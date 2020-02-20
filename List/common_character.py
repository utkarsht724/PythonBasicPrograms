def common_character():
    list1=[]
    list2=[]
    length=int(input("enter the length of the in a list"))
    for i in range(length):
        l1=int(input("enter the element in first list"))
        list1.append(l1)

        l2=int(input("enter the element in second list"))
        list2.append(l2)

    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                print("character are same:",list1[i])

common_character()
