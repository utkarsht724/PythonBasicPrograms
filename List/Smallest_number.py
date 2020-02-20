def smallest_number():
    list=[]
    for i in range(5):
        smallest=int(input("enter the element in list"))
        list.append(smallest)
        print(list)
    print("the minimum element in the list",min(list))
smallest_number()