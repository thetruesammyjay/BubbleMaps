import httpx
from typing import Optional, Dict, Any
from utils.helpers import async_retry

class BubblemapsAPI:
    BASE_URL = "https://api-legacy.bubblemaps.io"
    
    def __init__(self):
        self.client = httpx.AsyncClient()
    
    @async_retry(max_retries=3)
    async def check_map_availability(self, chain: str, token: str) -> bool:
        """Check if bubble map is available for token."""
        response = await self.client.get(
            f"{self.BASE_URL}/map-availability",
            params={"chain": chain, "token": token}
        )
        data = response.json()
        return data.get("status") == "OK" and data.get("availability", False)
    
    @async_retry(max_retries=3)
    async def get_map_metadata(self, chain: str, token: str) -> Optional[Dict[str, Any]]:
        """Get decentralization score and metadata."""
        response = await self.client.get(
            f"{self.BASE_URL}/map-metadata",
            params={"chain": chain, "token": token}
        )
        return response.json() if response.status_code == 200 else None
    
    @async_retry(max_retries=3)
    async def get_map_data(self, chain: str, token: str) -> Optional[Dict[str, Any]]:
        """Get detailed holder and transaction data."""
        response = await self.client.get(
            f"{self.BASE_URL}/map-data",
            params={"chain": chain, "token": token}
        )
        return response.json() if response.status_code == 200 else None