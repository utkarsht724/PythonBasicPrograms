#program to convert a list into nested dictionaries of keys

my_list=[1,2,3,4,5,6,7]
new_dict=current={}
for name in my_list:
    current[name]={}
    current=current[name]
