#program to check two list are identical
list1 = []
list2 = []
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
if list1==list2:
    print("list are identical")
else:
    print("list are not identical")