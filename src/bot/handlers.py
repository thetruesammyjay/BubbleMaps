from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
    CallbackQueryHandler
)
from services.bubblemaps import BubblemapsAPI
from services.market import MarketData
from services.screenshot import capture_bubblemap
from utils.analysis import analyze_token_data
from utils.chains import detect_chain
from .responses import format_token_report
from .keyboards import create_analysis_keyboard

async def start(update: Update, context: CallbackContext):
    """Send welcome message."""
    await update.message.reply_text(
        "🚀 Welcome to Bubblemaps Bot!\n\n"
        "Send me any token contract address to analyze its distribution."
    )

async def handle_address(update: Update, context: CallbackContext):
    """Process token contract address."""
    contract_address = update.message.text.strip()
    chain = detect_chain(contract_address) or "eth"  # Default to Ethereum
    
    bubblemaps = BubblemapsAPI()
    market = MarketData()
    
    # Check map availability
    if not await bubblemaps.check_map_availability(chain, contract_address):
        await update.message.reply_text("⚠️ Bubble map not available for this token.")
        return
    
    # Get data concurrently
    metadata, map_data, market_data, screenshot = await asyncio.gather(
        bubblemaps.get_map_metadata(chain, contract_address),
        bubblemaps.get_map_data(chain, contract_address),
        market.get_token_data(contract_address),
        capture_bubblemap(chain, contract_address)
    )
    
    if not all([metadata, map_data, screenshot]):
        await update.message.reply_text("❌ Error fetching token data.")
        return
    
    analysis = analyze_token_data(map_data, metadata, market_data)
    report = format_token_report(analysis)
    
    await update.message.reply_photo(
        photo=screenshot,
        caption=report['caption'],
        reply_markup=create_analysis_keyboard(contract_address)
    )
    await update.message.reply_text(
        report['details'],
        parse_mode='Markdown'
    )

async def handle_callback(update: Update, context: CallbackContext):
    """Handle inline button callbacks."""
    query = update.callback_query
    await query.answer()
    
    # Handle different callback actions
    if query.data.startswith('whales_'):
        contract_address = query.data.split('_')[1]
        # Implement whale details response
        await query.edit_message_text(text=f"Whale details for {contract_address}")

async def error_handler(update: Update, context: CallbackContext):
    """Log errors."""
    print(f"Update {update} caused error {context.error}")

def setup_handlers(application: Application):
    """Register all handlers."""
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_address))
    application.add_handler(CallbackQueryHandler(handle_callback))
    application.add_error_handler(error_handler)