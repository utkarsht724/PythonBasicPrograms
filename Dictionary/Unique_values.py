#program to print unique values in dictionary
def unique_value():
    my_dict={"x":3,"v":4,"j":9,"f":4,"i":9}
    print(my_dict)
    u_value=set(value for dic in my_dict for value in my_dict.values())
    print("the unique values ",u_value)

unique_value()