import yfinance as yf
import matplotlib.pyplot as plt

portfolio = {
    'AAPL' : 10,
    'TSLA' : 5,
    'MSFT' : 8
}

prices = {}
for symbol in portfolio:
    stock = yf.Ticker(symbol)
    prices[symbol] = stock.history(period="1d")['Close'].iloc[0]

print(prices)

total_value = 0
for symbol, quantity in portfolio.items():
    value = prices[symbol] * quantity
    total_value += value
    print(f"{symbol}: {quantity} shares x ${prices[symbol]:.2f} = ${value:.2f}")

print(f"Total Portfolio Value: ${total_value:.2f}")


for symbol in portfolio:
    stock = yf.Ticker(symbol)
    hist = stock.history(period="2d")
    today_close = hist['Close'].iloc[-1]
    yesterday_close = hist['Close'].iloc[-2]
    daily_change = ((today_close - yesterday_close) / yesterday_close) * 100
    print(f"{symbol} daily change: {daily_change:.2f}%")


# Chart
symbols = list(portfolio.keys())
values = [prices[s] * portfolio[s] for s in symbols]

plt.bar(symbols, values, color='skyblue')
plt.title("Portfolio Value Breakdown")
plt.ylabel("Value ($)")
plt.show()