from array import *
arr = array('i',[])
arr_length=int(input("enter the Length of the array:"))
for number in range(arr_length):
    x=int(input("enter the next element of array"))
    arr.append(x)
for i in range(arr_length,arr[0]):
 print(arr)
