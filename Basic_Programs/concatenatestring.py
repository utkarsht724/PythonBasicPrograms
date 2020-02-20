#program to concatenate all elements in a list into a string
def concatenate_list(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list([1,2,3,4,5]))