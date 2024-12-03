from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from creds import MongoDB_username, MongoDB_password

MONGODB_URI = f"mongodb+srv://{MongoDB_username}:{MongoDB_password}@cluster0.xkokyty.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'sample_trades' database
db = client.sample_trades

app = FastAPI()

crypto_data = ({})
investment_data = ({})

@app.get('/')
def root():
    return {"Hello": "World"}


""":returns every assets data"""
@app.get('/tickers')
def get_ticker() -> dict:
    
    assets_collection = db.assets # Get reference to 'assets' collection

    cursor = assets_collection.find({})
    for doc in cursor:
        del(doc['_id'])
        crypto_data[doc['asset_symbol']] = doc
    
    return crypto_data

""":returns particular asset data"""
@app.get('/tickers/{ticker_symbol}')
def get_ticker_data(ticker_symbol: str) -> dict:

    assets_collection = db.assets # Get reference to 'assets' collection
    document_to_find = {"asset_symbol" : ticker_symbol} # Query by 'asset_symbol'

    # Write an expression that retrieves the document matching  the query constraint in the 'assets' collection
    result = assets_collection.find_one(document_to_find)

    if result:
        res = dict({})
        del(result['_id'])    

        res[ticker_symbol] = result
        return res
    else:
        raise HTTPException(status_code = 404, detail = f"Ticker {ticker_symbol} not found")

""":returns particular asset sparkline"""
@app.get('/tickers/{ticker_symbol}/sparkline')
def get_ticker_sparkline(ticker_symbol: str) -> dict:

    assets_collection = db.assets # Get reference to 'assets' collection
    documnet_to_find = {"asset_symbol" : ticker_symbol} # Query by 'asset_symbol'

    result = assets_collection.find_one(documnet_to_find)

    if result:
        del(result['_id'])
        return {'name' : result['asset_name'], 'sparkline' : result['asset_sparkline']}
    else:
        raise HTTPException(status_code = 404, detail = f"Ticker {ticker_symbol} not found")

""":returns particular asset marketcap"""
@app.get('/tickers/{ticker_symbol}/marketcap')
def get_ticker_marketcap(ticker_symbol: str) -> dict:
    assets_collection = db.assets # Get reference to 'assets' collection
    documnet_to_find = {"asset_symbol" : ticker_symbol} # Query by 'asset_symbol'

    result = assets_collection.find_one(documnet_to_find)

    if result:
        del(result['_id'])
        return {'name' : result['asset_name'], 'marketCap' : result['asset_marketCap']}
    else:
        raise HTTPException(status_code = 404, detail = f"Ticker {ticker_symbol} not found")

""":returns particular asset change"""
@app.get('/tickers/{ticker_symbol}/change')
def get_ticker_change(ticker_symbol: str) -> dict:
    assets_collection = db.assets # Get reference to 'assets' collection
    documnet_to_find = {"asset_symbol" : ticker_symbol} # Query by 'asset_symbol'
    result = assets_collection.find_one(documnet_to_find)

    if result:
        del(result['_id'])
        return {'name' : result['asset_name'], 'change' : result['asset_change']}
    else:
        raise HTTPException(status_code = 404, detail = f"Ticker {ticker_symbol} not found")

""":returns particular asset price"""
@app.get('/tickers/{ticker_symbol}/price')
def get_ticker_price(ticker_symbol: str) -> dict:
    assets_collection = db.assets # Get reference to 'assets' collection
    documnet_to_find = {"asset_symbol" : ticker_symbol} # Query by 'asset_symbol'

    result = assets_collection.find_one(documnet_to_find)

    if result:
        del(result['_id'])
        return {'name' : result['asset_name'], 'price' : result['asset_price']}
    else:
        raise HTTPException(status_code = 404, detail = f"Ticker {ticker_symbol} not found")

""":returns particular asset rank"""
@app.get('/tickers/{ticker_symbol}/rank')
def get_ticker_rank(ticker_symbol: str) -> dict:
    assets_collection = db.assets # Get reference to 'assets' collection
    documnet_to_find = {"asset_symbol" : ticker_symbol} # Query by 'asset_symbol'

    result = assets_collection.find_one(documnet_to_find)

    if result:
        del(result['_id'])
        return {'name' : result['asset_name'], 'rank' : result['asset_rank']}
    else:
        raise HTTPException(status_code = 404, detail = f"Ticker {ticker_symbol} not found")

""":returns particular asset investment"""
@app.get('/tickers/{ticker_symbol}/investment')
def get_ticker_investment(ticker_symbol: str) -> dict:

    investment_collection = db.investment # Get reference to 'investment' collection
    documnet_to_find = {"asset_symbol" : ticker_symbol} # Query by 'asset_symbol'

    result = investment_collection.find_one(documnet_to_find)

    if result:
        del(result['_id'])
        return result
    else:
        raise HTTPException(status_code = 404, detail = f"Ticker {ticker_symbol} not found")


""":returns every assets investment"""
@app.get('/investment')
def get_total_investment() -> dict:
    investment_collection = db.investment # Get reference to 'investment' collection
    cursor = investment_collection.find({}) # Query by 'asset_symbol'

    for doc in cursor:
        del(doc['_id'])
        investment_data[doc['asset_symbol']] = doc

    return investment_data


client.close()