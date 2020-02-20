#PROGRAM TO REMOVE A KEY FROM DICTIONARY
def Remove():
    My_dic={1:2,3:9,4:7,6:8}
    print(My_dic)
    key=int(input("enter a key which u want to delete:"))
    if key in My_dic:
        del My_dic[key]
        print(My_dic)
    else:
        print("invalid input")
Remove()