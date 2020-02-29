
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

a= sns.load_dataset("data/gapminder-FiveYearData")
sns.boxplot(x='lifeExp',data=a)
plt.show()

