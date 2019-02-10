import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

#loading the data from seaborn's github
df = sns.load_dataset("iris")
#plotting using the seaborn data
sns.pairplot(df, hue="species")
#displaying the diagrams
plt.show()
