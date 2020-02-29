import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

a= sns.load_dataset("tips")
sns.barplot(x="sex",y="total_bill",data=a)
plt.show()