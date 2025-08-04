import requests # Import requests library to send get requests
import json # Import json library to parse JSON files to Python

url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing" # Set URL to the hidden API

coins = [] # Create empty list to store all coins

for start in range(1, 10001, 100):
    querystring = { # Define the query string with the parameters send to the API
        "start":f"{start}", # Crypto to start from (we iterate this to get all data)
        "limit":"100", # Number of Cryptos to request
        "sortBy":"market_cap", # Sorting of the cryptos (we can use whatever we want - its just important not to change it so the changing start always gives us new coins)
        "sortType":"desc", # How to sort
        "convert":"USD", # Currencies to convert to
        "cryptoType":"all",
        "tagType":"all",
        "audited":"false",
        "aux":""
        }

    payload = "" # Define empty payload (no payload is needed for the get request)
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"} # Define user agent (we want to be chrome)

    response = requests.get(url, data=payload, headers=headers, params=querystring) # Get the response of the API
    data = json.loads(response.text) # Parse the response from JSON to a list of dictionaries in Python
    for coin in data['data']['cryptoCurrencyList']: # Iterate over the inner list cryptoCurrencyList to get all the coins on the site
        id = coin['id'] # Store the id of the coin
        name = coin['name'] # Store the name of the coin
        for quote in coin['quotes']: # Iterate over the different quotes and find price in USD
            if quote['name'] == 'USD':
                price = quote['price'] # Store the price in USD
        coins.append( # Append the data as a dictionary to the outer list coins that stores all the coins
            {
                'id': id,
                'name': name,
                'price': price
            }
        )

# Print the results
print('ID\tName\tPrice'.expandtabs(30))
for coin in coins[:3]:
    print(f"{coin['id']}\t{coin['name']}\t{coin['price']}".expandtabs(35))        