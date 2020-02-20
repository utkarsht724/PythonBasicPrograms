try:
    C=1
except NameError:
    print("variable is not defined")
else:
    print("variable is defined")
try:
    B
except NameError:
    print("variable is not defined")
else:
    print("variable is defined")