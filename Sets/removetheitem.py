A={1,2,3,4,5}
item=int(input("enter an element you want to found"))
if item in A:
    print("elemnt is found",item)
    print("now remove that element from set")
    A.remove(item)
    print(A)
else:
    print(" please enter a valid element")
