from matplotlib import pyplot as plt
from matplotlib import style
a=[1,2,3]
y=[5,6,7]
plt.plot(a,y,'g',label='data')
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()