import pytest
from unittest.mock import AsyncMock, MagicMock
from bot.handlers import handle_address

@pytest.mark.asyncio
async def test_handle_address():
    update = MagicMock()
    context = MagicMock()
    update.message.text = "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
    
    await handle_address(update, context)
    update.message.reply_text.assert_called()