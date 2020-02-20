#program to represent first n character into lower string
str=input("enter the string")
n=int(input("enter value where u want to lower case"))

print(str)
print(str[:n].lower() + str[n:])