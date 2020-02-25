import pandas as pd
class Cal():
 def __init__(self,a,b):
        self.a=a
        self.b=b
 def add(self):
       return self.a+self.b
 def subtract(self):
     return self.a-self.b
 def multiply(self):
     return self.a*self.b
 def divide(self):
     return self.a/self.b
a=pd.Series([2,4,6,8,10])
b=pd.Series([1,3,5,7,9])

cl=Cal(a,b)
print("Addition of two panda series")
print(cl.add())
print()
print("Subtraction of two panda series")
print(cl.subtract())
print()
print("Multiplication of two panda series")
print(cl.multiply())
print()
print("Dividsion of two panda series")
print(cl.divide())