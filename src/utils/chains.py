from typing import Optional

def detect_chain(address: str) -> Optional[str]:
    """Simple chain detector based on address patterns."""
    address = address.lower()
    
    if address.startswith("0x") and len(address) == 42:
        return "eth"  # Default to Ethereum
    # Add more chain detection logic as needed
    return None