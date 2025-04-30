# Bubblemaps API Reference

## Endpoints

### Map Availability
`GET https://api-legacy.bubblemaps.io/map-availability`

Parameters:
- `chain` (string): Blockchain identifier (eth, bsc, etc)
- `token` (string): Contract address

### Map Metadata
`GET https://api-legacy.bubblemaps.io/map-metadata`

**Returns**:
- decentralisation_score
- identified_supply (CEX/contract percentages)
- last_update timestamp

### Map Data
`GET https://api-legacy.bubblemaps.io/map-data`

Returns detailed holder and transaction data.