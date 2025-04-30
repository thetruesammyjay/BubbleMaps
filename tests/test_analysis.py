from utils.analysis import analyze_token_data

def test_analyze_token_data():
    map_data = {
        "full_name": "Test Token",
        "symbol": "TEST",
        "nodes": [
            {"address": "0x1", "name": "Holder 1", "percentage": 10, "is_contract": False},
            {"address": "0x2", "name": "CEX", "percentage": 20, "is_contract": True}
        ]
    }
    metadata = {
        "decentralisation_score": 75,
        "identified_supply": {
            "percent_in_cexs": 15,
            "percent_in_contracts": 25
        }
    }
    
    result = analyze_token_data(map_data, metadata)
    assert result["basic_info"]["name"] == "Test Token"
    assert len(result["holders"]["top_5"]) == 2