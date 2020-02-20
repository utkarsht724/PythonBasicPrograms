def append():
    list1=[]
    list2=[]
    length = int(input("enter the length of list"))
    for i in range(length):
        lst1 = int(input("enter the next element of first list: "))
        list1.append(lst1)
    print("First list", list1)

    for j in range(length):
        lst2 = int(input("enter the next element of second list: "))
        list2.append(lst2)
    print("Second list", list2)
    print(" ")

    result=list1+list2
    print("after appending first and second list::",result)

append()
