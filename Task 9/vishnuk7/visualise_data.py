
#Import Libraries
import matplotlib.pyplot as plt
import pandas as pd

# Read DataFrame ( and parse axis dates)
df = pd.read_csv("INR.csv", usecols=['Date','Rate'], parse_dates=['Date'])
# Use Date as index
df.set_index('Date',inplace=True)
plt.title("Indian Rupess(INR) per US Dollar(USD)")
plt.xlabel("Months")
plt.ylabel("Indian Rupess to One U.S. Dollar")
plt.plot(df['Rate'])
plt.show()
