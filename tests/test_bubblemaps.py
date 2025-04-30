import pytest
from unittest.mock import AsyncMock
from services.bubblemaps import BubblemapsAPI

@pytest.mark.asyncio
async def test_check_map_availability():
    api = BubblemapsAPI()
    api.client = AsyncMock()
    api.client.get.return_value.json.return_value = {
        "status": "OK",
        "availability": True
    }
    
    result = await api.check_map_availability("eth", "0x123")
    assert result is True