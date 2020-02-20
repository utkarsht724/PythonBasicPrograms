#program to concatenate dictionary
def concatenate_dictionary():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    print("Sample Dictionary",dic1,dic2,dic3)

    final_dictionary={**dic1,**dic2,**dic3}

    print("Expected Dictionary",final_dictionary)

concatenate_dictionary()