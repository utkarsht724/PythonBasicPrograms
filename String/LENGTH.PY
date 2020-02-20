#program to print length og longest word in string
def longest_word_length():
    length=int(input("enter the lenegth of the list-"))
    list=[]
    for i in range(length):
        str=input("enter the element:")
        list.append(str)
        print(list)
    print("longest element in the list",max(list))
    print("length of longest element",len(max(list)))

longest_word_length()