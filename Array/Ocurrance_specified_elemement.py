#program to get the number of occurrences of a specified element in an array
from array import *
class occurance_specified_elelemet():
    def occurance(self):
        arr=array('i',[])
        arr_length = int(input("Enter the Length of the array:"))
        for x in range(arr_length):
            element=int(input("Enter the element "))
            arr.append(element)
        key_element=int(input("Enter the element u want to get the number of occurance"))
        print()
        if key_element in arr:
             print("The occurance of specified element is: ",arr.count(key_element))
        else:
            print()
            print("OOPS!!it seems to be error"
                "Try again")

specified_element=occurance_specified_elelemet()
specified_element.occurance()
