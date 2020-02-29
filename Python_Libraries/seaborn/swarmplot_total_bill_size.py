import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

a= sns.load_dataset("tips")
sns.swarmplot(x='total_bill',y='size',data=a)
plt.show()