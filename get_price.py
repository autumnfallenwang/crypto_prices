import requests
import pandas as pd

# Your list of coins you're interested in
coin_ids = ['bitcoin', 'ethereum', 'cosmos', 'automata', 'api3', 'alethea-artificial-liquid-intelligence-token', 'singularitynet', 'arkham', 'akropolis', 'arbitrum', 'beta-finance', 'nervos-network', 'centrifuge', 'chaingpt', 'clore-ai', 'contentos', 'concentrated-voting-power', 'dione', 'dymension', 'filecoin', 'fio-protocol', 'stafi', 'fetch-ai', 'graphlinq-protocol', 'camelot-token', 'gifto', 'gala', 'immutable-x', 'kaspa', 'labs-protocol', 'livepeer', 'lido-dao', 'myria', 'helium-mobile', 'metis-token', 'maker', 'nakamoto-games', 'nfprompt-token', 'orca', 'ondo-finance', 'ordinals', 'optimism', 'pepe', 'paal-ai', 'pnetwork', 'polymesh', 'pivx', 'pyth-network', 'constitutiondao', 'benqi', 'rally-2', 'thorchain', 'rei-network', 'reserve-rights-token', 'realio-network', 'render-token', 'sats-ordinals', 'havven', 'sui', 'sei-network', 'starknet', 'solana', 'ssv-network', 'bittensor', 'celestia', 'polytrade', 'trias-token', 'dejitaru-tsuka', 'troll', 'turbo', 'troy', 'verasity', 'viberate', 'vite', 'vidt-dao', 'voxies', 'worldcoin-wld', 'wink', 'wrapped-axelar', 'woo-network', 'chainge-finance', 'xai', 'zetachain', 'bitcoin-cats', 'wrapped-minima', 'arweave', 'hooked-protocol', 'sleepless-ai', 'memecoin-2', 'matic-network', 'the-graph', 'pendle', 'manta-network', 'altlayer', 'marlin', 'aptos', 'synapse-2', 'dydx-chain', 'dogecoin', 'floki']

# The URL for fetching prices from CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price"

# Parameters for the request: the coin IDs and the currency for the price
params = {
    'ids': ','.join(coin_ids),
    'vs_currencies': 'usd'
}

# Make the request to CoinGecko
response = requests.get(url, params=params)

# Parse the JSON response
prices = response.json()

# Convert the prices data to a more structured form for saving as a CSV
data = []
for coin_id in coin_ids:
    price = prices.get(coin_id, {}).get('usd', 'N/A')
    data.append({'coin_id': coin_id, 'usd_price': price})

# Convert the structured data into a pandas DataFrame
df = pd.DataFrame(data)

# Specify the CSV file path
csv_file_path = 'coin_prices.csv'  # Adjust the path as needed

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

