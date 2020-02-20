#program to remove indexes from given list

Sample_List= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Orginal list::",Sample_List)
del_index = [0, 4, 5]
for i in sorted(del_index, reverse=True):
    del Sample_List[i]

print(" ")
print("After removing element from liSt" ,Sample_List)
