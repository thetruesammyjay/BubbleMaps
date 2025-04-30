from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_analysis_keyboard(contract_address: str):
    """Create inline keyboard for token analysis options."""
    buttons = [
        [
            InlineKeyboardButton("🐋 Whales", callback_data=f"whales_{contract_address}"),
            InlineKeyboardButton("📊 Distribution", callback_data=f"dist_{contract_address}"),
        ],
        [
            InlineKeyboardButton("🔄 Transactions", callback_data=f"txs_{contract_address}"),
            InlineKeyboardButton("📈 Market Data", callback_data=f"market_{contract_address}"),
        ]
    ]
    return InlineKeyboardMarkup(buttons)