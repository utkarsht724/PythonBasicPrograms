#program to count the number of dictionary value that is a list
def list_to_dictionary():
    my_list=[1,1,1,2,3,4,4,5,6]
    my_dict={}
    for i in range(len(my_list)):
        my_dict[my_list[i]]  =  my_list.count(my_list[i])
    print(my_dict)

list_to_dictionary()

