import requests
from collections import OrderedDict
from pymongo import MongoClient
from creds import MongoDB_username, MongoDB_password
from strategy import sorted_investment

MONGODB_URI = f"mongodb+srv://{MongoDB_username}:{MongoDB_password}@cluster0.xkokyty.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'sample_trades' database
db = client.sample_trades

# Get reference to 'investment' collection
investment_collection = db.investment

requests = requests.get('http://127.0.0.1:8000/tickers')

data = requests.json()

investment = []

for key in data.keys():
    invest = OrderedDict({})
    invest = {
        'asset_name' : data[key]['asset_name'],
        'asset_symbol' : data[key]['asset_symbol'],
        'asset_price' : data[key]['asset_symbol'],
        'asset_marketCap' : data[key]['asset_marketCap'],
        'asset_investment' : str(sorted_investment[key]) # MongoDB can only handle up to 8-byte ints
    }

    investment.append(invest)

result = investment_collection.insert_many(investment)

client.close()
