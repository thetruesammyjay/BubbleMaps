def format_token_report(analysis: dict) -> dict:
    """Format token analysis into Telegram messages."""
    basic = analysis['basic_info']
    decen = analysis['decentralization']
    
    caption = f"📊 {basic['name']} ({basic['symbol']}) Bubble Map"
    
    details = (
        f"🌐 *Decentralization Score*: {decen['score']}/100\n\n"
        f"💰 *Price*: ${basic['price']:.4f}\n"
        f"📈 *Market Cap*: ${basic['market_cap']:,.2f}\n\n"
        f"🔍 *Supply Distribution*:\n"
        f"- CEXs: {decen['cex_percentage']}%\n"
        f"- Contracts: {decen['contract_percentage']}%\n\n"
        f"🏆 *Top 5 Holders*:\n"
    )
    
    for holder in analysis['holders']['top_5']:
        details += f"{holder['rank']}. {holder['name']} - {holder['percentage']}%\n"
    
    return {'caption': caption, 'details': details}