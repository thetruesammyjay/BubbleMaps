from typing import Dict, Any

def analyze_token_data(map_data: Dict, metadata: Dict, market_data: Dict = None) -> Dict[str, Any]:
    """Analyze and process token data from multiple sources."""
    analysis = {
        "basic_info": {
            "name": map_data.get("full_name", "Unknown"),
            "symbol": map_data.get("symbol", "?"),
            "price": market_data.get("price", 0) if market_data else 0,
            "market_cap": market_data.get("market_cap", 0) if market_data else 0
        },
        "decentralization": {
            "score": metadata.get("decentralisation_score", 0),
            "cex_percentage": metadata.get("identified_supply", {}).get("percent_in_cexs", 0),
            "contract_percentage": metadata.get("identified_supply", {}).get("percent_in_contracts", 0)
        },
        "holders": {
            "top_5": [],
            "whales": []
        }
    }
    
    # Process top 5 holders
    for i, node in enumerate(map_data.get("nodes", [])[:5], 1):
        analysis["holders"]["top_5"].append({
            "rank": i,
            "address": node.get("address"),
            "name": node.get("name", "Unknown"),
            "percentage": node.get("percentage", 0),
            "is_contract": node.get("is_contract", False)
        })
    
    # Identify whales (>5% holders)
    analysis["holders"]["whales"] = [
        node for node in map_data.get("nodes", [])
        if node.get("percentage", 0) > 5
    ]
    
    return analysis