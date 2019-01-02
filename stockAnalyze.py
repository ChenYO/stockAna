import twstock
import matplotlib.pyplot as plt
import pandas as pd

stock_5478 = twstock.Stock('5478')
stock_5478_2018 = stock_5478.fetch_from(2018, 1)
stock_5478_2018_pd = pd.DataFrame(stock_5478_2018)
stock_5478_2018_pd = stock_5478_2018_pd.set_index('date')

fig = plt.figure(figsize=(10, 6))
plt.plot(stock_5478_2018_pd.close, '-', label='Close Price')
plt.plot(stock_5478_2018_pd.high, '-', label='High Price')
plt.plot(stock_5478_2018_pd.open, '-', label='Open Price')
plt.title('5478 2018 open/close price figure', loc='right')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True, axis='y')
plt.legend()
fig.savefig('5478_2018.png')