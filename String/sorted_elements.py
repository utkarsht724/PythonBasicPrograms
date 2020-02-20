def elements():
    list=[]
    length=int(input("enter the length of list"))
    for i in range(length):
        str=input("enter the words in string")
        list.append(str)
    print("input list",list)
    print("sorted list",sorted(set(list)))
elements()



