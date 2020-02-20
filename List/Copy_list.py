def clone():
    list=[]
    m=[]
    length=int(input("enter the length of a list"))
    for value in range(length):
        number=int(input("enter the element in the list"))
        list.append(number)
        print("old list",list)
    m=list.copy()
    print("new list",m)

clone()