import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

a= sns.load_dataset("iris")
sns.violinplot(x='species',y='sepal_length',data=a)
plt.show()