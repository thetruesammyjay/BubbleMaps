# 🗺️ Bubblemaps Telegram Bot

A Telegram bot that analyzes token distribution using [Bubblemaps](https://bubblemaps.io/) API, providing:
- Token bubble map visualizations
- Decentralization scores
- Holder distribution analysis
- Whale tracking
- Market data integration

## 🌟 Features

- **Instant Bubble Maps**: Get visual token distribution charts for any supported contract
- **Comprehensive Analysis**:
  - Decentralization score (0-100)
  - CEX vs. contract holdings
  - Top holder identification
- **Market Data**: Price, market cap, volume (via CoinGecko)
- **Multi-Chain Support**: Ethereum, BSC, Polygon, and more
- **User-Friendly**: Simple interface with interactive buttons

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- Telegram Bot Token ([get one here](https://core.telegram.org/bots#6-botfather))
- Playwright browsers (installed automatically)

### Setup
```bash
# Clone repository
git clone https://github.com/thetruesammyjay/BubbleMaps.git
cd bubblemaps-telegram-bot

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
playwright install
```

## 🚀 Usage
1. Create a `.env` file:
```ini
TELEGRAM_BOT_TOKEN=your_bot_token_here
# Optional:
COINGECKO_API_KEY=your_key_here
```
2. Run the bot:
```bash
python src/main.py
```
3. In Telegram:

- Start a chat with your bot

- Send any token contract address (e.g., `0x1f9840a85d5af5bf1d1762f925bdaddc4201f984`)

- Receive analysis with interactive buttons

## 🏗️ Project Structure
```markdown
bubblemaps-telegram-bot/
├── src/
│   ├── bot/            # Telegram handlers and responses
│   ├── services/       # API integrations (Bubblemaps, CoinGecko)
│   ├── utils/          # Analysis and helper functions
│   └── main.py         # Entry point
├── tests/              # Unit tests
├── scripts/            # Utility scripts
└── docs/               # Documentation
```

## 🛠️ Development
### Code Quality Tools
```bash
# Type checking
mypy src/

# Linting
flake8 src/

# Testing
pytest tests/
```
### Dependency Management
- Update `requirements.txt`:
```bash
pip freeze > requirements.txt
```

## 🤝 Contributing
- Fork the project

- Create your feature branch (`git checkout -b feature/AmazingFeature`)

- Commit your changes (`git commit -m 'Add some amazing feature'`)

- Push to the branch (`git push origin feature/AmazingFeature`)

- Open a Pull Request

## 📄 License
**MIT License** – See [LICENSE](https://license.md/) for details

## 📬 Contact Us
- **X (Twitter):** [@thatbwoysammyj](https://x.com/thatbwoysammyj)  
- **Telegram:** [t.me/sammyjayisthename](https://t.me/sammyjayisthename)  
- **Email:** [thetruesammyjay@gmail.com](mailto:thetruesammyjay@gmail.com)
