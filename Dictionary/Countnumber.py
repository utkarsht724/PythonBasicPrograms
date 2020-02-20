#count the number in a list
my_dict={"a":[1,2,3],"b":[3,4,5],"c":[8,3,4]}
# count=0
# for x in my_dict:
#     if isinstance(my_dict[x],list):
#
#         count += len(my_dict[x])
# print(count)
ctr=sum(map(len ,my_dict.values()))
print(ctr)