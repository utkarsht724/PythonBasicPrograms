import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


a= sns.load_dataset("titanic")


sns.pointplot(x='survived',y='sex', hue="class",data=a)
plt.show()