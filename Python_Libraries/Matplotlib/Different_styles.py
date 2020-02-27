from matplotlib import pyplot as plt
from matplotlib import style

x=[5,10,20]
y=[6,8,14]
a=[4,8,14]
n=[9,5,14]


plt.plot(x,'g',label='Students',linewidth=3)
plt.plot(a,n,'c',label='class',linewidth=5)
plt.title("student data")
plt.xlabel("students")
plt.ylabel("class")
plt.legend()
plt.show()
