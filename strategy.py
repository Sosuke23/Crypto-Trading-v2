import requests
import numpy as np

requests = requests.get('http://127.0.0.1:8000/tickers')
data = requests.json()

sparkline, slopes, normalized_slope, total_slope = dict({}), dict({}), dict({}), 0
change, normalized_change, total_change = dict({}), dict({}), 0
marketCap, inverse_marketCap, normalized_marketCap, total_marketCap = dict({}), dict({}), dict({}), 0

investment = dict({})
combine_factor = dict({}) # Sparkline(40%), Change(30%), MarketCap(30%)

investment_amount = 1000000

for key in data.keys():
    sparkline[key] = [float(x) for x in data[key]['asset_sparkline']]
    change[key] = float(data[key]['asset_change'])
    marketCap[key] = float(data[key]['asset_marketCap'])


for (key, val) in sparkline.items():
    x = np.arange(len(val))
    slope, intercept = np.polyfit(x, val, 1)
    total_slope += slope
    slopes[key] = slope

# Normalize the slope to ensure comparability across assets and allocate investments proportionally.
for (key, val) in slopes.items():
    normalized_slope[key] = float(val) / total_slope


for (key, val) in marketCap.items():
    inverse_marketCap[key] = 1 / val
    total_marketCap += inverse_marketCap[key]

# Normalize the marketCap to ensure comparability across assets and allocate investments proportionally.
for (key, val) in inverse_marketCap.items():
    normalized_marketCap[key] = inverse_marketCap[key] / total_marketCap


# Normalize the change % to ensure comparability across assets and allocate investments proportionally.
total_change = sum([abs(x) for x in change.values()])
for (key, val) in change.items():
    normalized_change[key] = abs(val) / total_change


for key in data.keys():
    combine_factor[key] = 0.3 * normalized_marketCap[key] + 0.3 * normalized_change[key] + 0.4 * normalized_slope[key]

# Calculate the amount to invest in each asset
for key in data.keys():
    investment[key] = max(0, combine_factor[key] * investment_amount)

# Sorting using invested amount (Decreasing)
sorted_investment = dict(sorted(investment.items(), key = lambda item: item[1], reverse = True))