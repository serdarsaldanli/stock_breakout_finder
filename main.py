import yfinance as yf
from datetime import date
import pandas as pd


def find_stock_breakout(symbol, start_date, end_date):
  try:
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    if stock_data.empty:
      print(f"{symbol} için uygun veri yok.")
      return None, None

    max_price = stock_data["Close"].max()
    breakout_date = stock_data[stock_data["Close"] ==
                               max_price].index[-1].strftime('%Y-%m-%d')
    return max_price, breakout_date
  except Exception as e:
    print(f"Hata oluştu: {e}")
    return None, None


df = pd.read_csv('stock_list.csv', delimiter=",")
stock_symbols = [list(row) for row in df.values]

print("Önceki zirveyi aşan stoklar:")

for symbol in stock_symbols:
  max_price, breakout_date = find_stock_breakout(symbol, "2023-01-01",
                                                 date.today())

  if max_price is not None and breakout_date is not None:
    max_price = round(max_price, 2)
    print(f"{symbol}: {max_price} (Zirve Tarihi: {breakout_date})")

print("En güncel zirve yapan stoklar:")

latest_breakouts = []

for symbol in stock_symbols:
  max_price, breakout_date = find_stock_breakout(symbol, "2023-01-01",
                                                 date.today())

  if max_price is not None and breakout_date is not None:
    max_price = round(max_price, 2)
    latest_breakouts.append((symbol, max_price, breakout_date))

latest_breakouts.sort(key=lambda x: x[2], reverse=True)

for symbol, max_price, breakout_date in latest_breakouts:
  print(f"{symbol}: {max_price} (Zirve Tarihi: {breakout_date})")

