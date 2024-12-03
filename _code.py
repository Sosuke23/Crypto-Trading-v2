import requests
import math
from collections import OrderedDict
from pymongo import MongoClient
from creds import MongoDB_username, MongoDB_password

MONGODB_URI = f"mongodb+srv://{MongoDB_username}:{MongoDB_password}@cluster0.xkokyty.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'sample_trades' database
db = client.sample_trades

# Get reference to 'investment' collection
assets_collection = db.investment

requests = requests.get('http://127.0.0.1:8000/tickers')

data = requests.json()

data_len = len(data)
invest = [0] * data_len

portfolio_size = input("Enter the value of your portfolio: ")

try:
    val = float(portfolio_size)
except ValueError:
    print("Enter a valid amount \nTry again")
    portfolio_size = input("Enter the value of your portfolio: ")

position_size = float(portfolio_size) / data_len

investment = []

for key in data.keys():
    di = OrderedDict({})
    di = {
        'asset_name' : data[key]['asset_name'],
        'asset_symbol' : data[key]['asset_symbol'],
        'asset_price' : data[key]['asset_symbol'],
        'asset_marketCap' : data[key]['asset_marketCap'],
        'asset_investment' : str(math.floor(position_size / float(data[key]['asset_price']))) # MongoDB can only handle up to 8-byte ints
    }

    investment.append(di)

result = assets_collection.insert_many(investment)

client.close()
