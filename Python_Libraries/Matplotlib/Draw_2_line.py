#Write a Python program to plot two or more lines on same plot with suitable legends of from matplotlib
from matplotlib import pyplot as plt
from matplotlib import style
x=[5,8,10]
y=[12,16,30]
z=[6,9,11]

#c=[8,9,10]

plt.plot(x,y,label='line one')
plt.plot(z,label="line two")
plt.title("info")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.show()