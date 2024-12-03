# Crypto Trading

## Strategy
This project implements a data-driven strategy to allocate investment across various cryptocurrencies based on three key factors: **Market Cap**, **Price Change**, and **Price Trend (Slope)**. The strategy aims to maximize returns by considering each cryptocurrency's market dominance, recent performance, and momentum.

The core steps of the strategy include:
1. **Market Cap Normalization**: Adjusting the weight of each asset based on its market capitalization.
2. **Change Normalization**: Considering the recent price change (percentage change in the last 24 hours) of each asset.
3. **Slope Calculation**: Using linear regression to calculate the price trend (slope) over the past day.

These factors are combined using predefined weights (**30%** for Market Cap, **30%** for Change, and **40%** for Slope) to generate a final investment allocation for each asset. The investment is then distributed accordingly, with the highest amounts going to assets with the most favorable combined factors.

This approach helps to diversify investments while targeting assets with high growth potential based on their market dynamics.

The investment data is then uploaded into a MongoDB database for further use, analysis, or tracking.

## API Interface

### Endpoints

- `/tickers`: Returns data for all assets in the database.
```json
{
  "BTC": {
    "asset_name": "Bitcoin",
    "asset_symbol": "BTC",
    "asset_price": "95186.30247607821",
    "asset_marketCap": "1883765481892",
    "asset_change": "-1.68",
    "asset_rank": "1",
    "asset_sparkline": [
      "96870.6691464183",
      "97024.06873786346",
      "97025.74133365744",
      "97144.31853951991",
      "97208.51877532457",
      "97196.24591895995",
      "97275.84061985565",
      "97218.53539010396",
      "97377.44731776966",
      "97157.01092261533",
      "97027.57090773877",
      "97374.10944346579",
      "97597.43598684136",
      "97553.40962705879",
      "97353.89008262115",
      "97763.88952775756",
      "97706.84707717874",
      "97368.30579656793",
      "96551.13300867053",
      "96729.48085109692",
      "96326.54310800624",
      "96156.49995856064",
      "95505.44677001836",
      "95302.34985439564"
    ]
  },
  "ETH": {
    "asset_name": "Ethereum",
    "asset_symbol": "ETH",
    "asset_price": "3596.738493512206",
    "asset_marketCap": "433199405531",
    "asset_change": "-2.46",
    "asset_rank": "2",
    "asset_sparkline": [
      "3690.1182691543145",
      "3690.299096992927",
      "3689.1891747360346",
      "3700.8125058907376",
      "3707.0067629693863",
      "3722.895942981123",
      "3733.1254519795375",
      "3716.559067847192",
      "3722.064702981301",
      "3707.563638274544",
      "3692.0897158477082",
      "3698.4786179686507",
      "3723.5206440439",
      "3718.5934420551903",
      "3709.3868584366314",
      "3721.27860198859",
      "3719.840477264152",
      "3733.656721974856",
      "3679.738376336494",
      "3694.446492914165",
      "3675.6631501666707",
      "3671.861260554078",
      "3631.816157433993",
      "3613.9888664365926"
    ]
  },......}
```
- `/tickers/{ticker_symbol}`: Fetches data for a specific asset by its symbol.
```json
{
  "BTC": {
    "asset_name": "Bitcoin",
    "asset_symbol": "BTC",
    "asset_price": "95186.30247607821",
    "asset_marketCap": "1883765481892",
    "asset_change": "-1.68",
    "asset_rank": "1",
    "asset_sparkline": [
      "96870.6691464183",
      "97024.06873786346",
      "97025.74133365744",
      "97144.31853951991",
      "97208.51877532457",
      "97196.24591895995",
      "97275.84061985565",
      "97218.53539010396",
      "97377.44731776966",
      "97157.01092261533",
      "97027.57090773877",
      "97374.10944346579",
      "97597.43598684136",
      "97553.40962705879",
      "97353.89008262115",
      "97763.88952775756",
      "97706.84707717874",
      "97368.30579656793",
      "96551.13300867053",
      "96729.48085109692",
      "96326.54310800624",
      "96156.49995856064",
      "95505.44677001836",
      "95302.34985439564"
    ]
  }
}
```
- `/tickers/{ticker_symbol}/sparkline`, `/tickers/{ticker_symbol}/marketcap`, `/tickers/{ticker_symbol}/change`, `/tickers/{ticker_symbol}/price`, `/tickers/{ticker_symbol}/rank`: Return specific asset details.
```json
{
  "name": "Bitcoin",
  "sparkline": [
    "96870.6691464183",
    "97024.06873786346",
    "97025.74133365744",
    "97144.31853951991",
    "97208.51877532457",
    "97196.24591895995",
    "97275.84061985565",
    "97218.53539010396",
    "97377.44731776966",
    "97157.01092261533",
    "97027.57090773877",
    "97374.10944346579",
    "97597.43598684136",
    "97553.40962705879",
    "97353.89008262115",
    "97763.88952775756",
    "97706.84707717874",
    "97368.30579656793",
    "96551.13300867053",
    "96729.48085109692",
    "96326.54310800624",
    "96156.49995856064",
    "95505.44677001836",
    "95302.34985439564"
  ]
}
```
```json
{
  "name": "Bitcoin",
  "marketCap": "1883765481892"
}
```
```json
{
  "name": "Bitcoin",
  "change": "-1.68"
}
```
```json
{
  "name": "Bitcoin",
  "price": "95186.30247607821"
}
```
```json
{
  "name": "Bitcoin",
  "rank": "1"
}
```
- `/investment`: Fetches the investment data for all assets.
```json
{
  "BTC": {
    "asset_name": "Bitcoin",
    "asset_symbol": "BTC",
    "asset_price": "BTC",
    "asset_marketCap": "1883765481892",
    "asset_investment": "207497.90531477178"
  },
  "ETH": {
    "asset_name": "Ethereum",
    "asset_symbol": "ETH",
    "asset_price": "ETH",
    "asset_marketCap": "433199405531",
    "asset_investment": "9460.14044491497"
  },
  "USDT": {
    "asset_name": "TetherUSD",
    "asset_symbol": "USDT",
    "asset_price": "USDT",
    "asset_marketCap": "134231114694",
    "asset_investment": "7.463412925471012"
  },
  "BNB": {
    "asset_name": "BNB",
    "asset_symbol": "BNB",
    "asset_price": "BNB",
    "asset_marketCap": "95502850503",
    "asset_investment": "3507.6945845709733"
  },
  "USDC": {
    "asset_name": "USDC",
    "asset_symbol": "USDC",
    "asset_price": "USDC",
    "asset_marketCap": "39975727648",
    "asset_investment": "8.341786200942877"
  },
  "XRP": {
    "asset_name": "XRP",
    "asset_symbol": "XRP",
    "asset_price": "XRP",
    "asset_marketCap": "131666044543",
    "asset_investment": "5883.238130469943"
  },....}
```
- `/tickers/{ticker_symbol}/investment`: Fetches the investment data for a specific asset.
```json
{
  "asset_name": "Bitcoin",
  "asset_symbol": "BTC",
  "asset_price": "BTC",
  "asset_marketCap": "1883765481892",
  "asset_investment": "207497.90531477178"
}
```

