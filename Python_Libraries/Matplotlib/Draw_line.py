#Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title
from matplotlib import pyplot as plt
x=[5,8,10]
y=[6,9,18]
plt.plot(x,y)
plt.title("epic info")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()