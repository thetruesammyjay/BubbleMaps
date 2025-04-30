import os
from dotenv import load_dotenv

def setup():
    """Initial bot setup script."""
    load_dotenv()
    
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("TELEGRAM_BOT_TOKEN=your_token_here\n")
            f.write("BUBBLEMAPS_API_KEY=optional\n")
            f.write("COINGECKO_API_KEY=optional\n")
        
        print("Created .env file. Please update with your credentials.")
    
    print("Setup complete. Install dependencies with: pip install -r requirements.txt")

if __name__ == "__main__":
    setup()