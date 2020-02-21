from array import *
class occurance_specified_element():
    def occurance(self):
        arr=array('i',[])
        arr_length = int(input("Enter the Length of the array:"))
        for x in range(arr_length):
            element=int(input("Enter the element: "))
            arr.append(element)
        print("Original array : ", arr)
        print()

        key_element=int(input("Enter the element u want to remove the first occurance: "))
        print()
        if key_element in arr:
             ("remove element is: ",arr.remove(key_element))

             print("New array: ",arr)
        else:
            print()
            print("OOPS!!it seems to be error"
                "Try again")

specified_element=occurance_specified_element()
specified_element.occurance()
