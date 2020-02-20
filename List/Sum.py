def add_element():
    list=[]
    sum=0
    length = int(input("enter the length of list"))
    for value in range(length):
        number=int(input("enter the number"))
        list.append(number)
        print(list)
    for num in range(len(list)):
        sum += (list[num])
    print(" ")
    print("the sum of element in list::",sum)
add_element()