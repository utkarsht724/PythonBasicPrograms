from matplotlib import pyplot as plt
from matplotlib import style
x=[5,8,10]
y=[12,16,30]
z=[6,9,11]

#c=[8,9,10]

plt.plot(x,y,'g',label='line one',linewidth=5)
plt.plot(z,'c',label="line two",linewidth=2)
plt.title("info")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()
