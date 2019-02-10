import numpy as np,pandas as pd,matplotlib.pyplot as plt

data = pd.read_csv('bitcoin_dataset.csv')
data.head()
data['Date'] = pd.to_datetime(data['Date'].values)
date = data['Date'].values
price = data['btc_market_price'].values
plt.plot(date, price)
plt.title("Bitcoin Price")
plt.xlabel("Year")
plt.ylabel("Price")
plt.axis(['2009', '2018', 0, 2000])
plt.show()