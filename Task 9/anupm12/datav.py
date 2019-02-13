import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("monthly_csv.csv", usecols=['Date','Price'], parse_dates=['Date'])
df.set_index('Date',inplace=True)
plt.xlabel("Months", fontsize=10)
plt.ylabel("Monthly gold rate", fontsize=10)
plt.plot(df['Price'], color="#341f97")
plt.title("Gold rates")
plt.show()