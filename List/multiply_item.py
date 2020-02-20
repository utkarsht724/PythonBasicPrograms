def multiplication():
    list=[]
    result=1
    for value in range(0,5):
        number=int(input("enter a number"))
        list.append(number)
    print(list)

    for num in range(len(list)):
        result *= list[i]
    print("the multiplication of element in list::",result)

multiplication()


#