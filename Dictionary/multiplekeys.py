#program to Check multiple keys exist in a dictionary

def Multiple_keys():

    sports = {"name": "xyz", "age": 22, "sex": "male"}

# using comparison operator

    print(sports.keys() >= {"name", "age"})
    print(sports.keys() >= {"sex", "name"})
    print(sports.keys() >= {"sex", "fullname"})
    print(sports.keys() >= {"age", "sex"})

Multiple_keys()
