import requests
import pandas as pd

def get_coingecko_coins():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    coins = response.json()
    return coins

def save_coins_to_csv(coins, file_path):
    coins_df = pd.DataFrame(coins)
    coins_df.to_csv(file_path, index=False)
    print(f"Coins list saved to {file_path}")

# Fetch the list of coins from CoinGecko
coins_list = get_coingecko_coins()

# Specify the path where you want to save the CSV file
file_path = 'coingecko_coins_list.csv'

# Save the coins list to a CSV file
save_coins_to_csv(coins_list, file_path)

