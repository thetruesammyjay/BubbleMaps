import httpx
from typing import Optional, Dict

class MarketData:
    COINGECKO_API = "https://api.coingecko.com/api/v3"
    
    def __init__(self):
        self.client = httpx.AsyncClient()
    
    async def get_token_data(self, contract_address: str) -> Optional[Dict]:
        """Get market data for token."""
        try:
            response = await self.client.get(
                f"{self.COINGECKO_API}/coins/ethereum/contract/{contract_address}",
                params={"localization": "false", "tickers": "false"}
            )
            if response.status_code == 200:
                data = response.json()
                return {
                    "price": data["market_data"]["current_price"]["usd"],
                    "market_cap": data["market_data"]["market_cap"]["usd"],
                    "volume": data["market_data"]["total_volume"]["usd"]
                }
        except Exception:
            return None
        return None