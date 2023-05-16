import requests  #importing the requests library to handle the usage of an API

# URL of the Coingecko API
url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,fantom,bitcoin&vs_currencies=usd" #In this case, we have it filtered to include fantom, bitcoin, and ethereum. You can add currencies as needed.

# Send a GET request to the Coingecko API
response = requests.get(url)

# Parse the API response as JSON
data = response.json()

# Extraction code for various crypto currencies. Apply the same code format below to add currencies. 
if "ethereum" in data and "usd" in data["ethereum"]:
    ethereum_price = data["ethereum"]["usd"]
    print(f"Ethereum price: {ethereum_price}")
else:
    print("Failed to retrieve Ethereum's price.")

if "fantom" in data and "usd" in data["fantom"]:
    fantom_price = data["fantom"]["usd"]
    print(f"Fantom price: {fantom_price}")
else:
    print("Failed to retrieve Fantom's price.")

if "bitcoin" in data and "usd" in data["bitcoin"]:
    bitcoin_price = data["bitcoin"]["usd"]
    print(f"Bitcoin price: {bitcoin_price}")
else:
    print("Failed to retrieve Bitcoin's price.")
