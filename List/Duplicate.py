def Duplicate():
    list=[]
    length=int(input("enter the length of the string"))
    for i in range(length):
        number=int(input("enter the next element of the list"))
        if number not in list:
            list.append(number)
        print(list)

Duplicate()

