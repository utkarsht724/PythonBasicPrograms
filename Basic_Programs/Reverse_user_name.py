class Reverse_user:
 try:
     def Reverse_user_name(self):
         print("  The name of user is:",first_name," ",last_name)
         str=""
         name =(first_name, "  ", last_name ,"   Reverse order of name is: ",)


         for i in name:
             str = i +  str
         print(str)
 except Exception as e:
     print("ERROOR",type(e))
Rev = Reverse_user()

first_name=input("enter the first name of the user: ")
last_name=input("enter the last name of the user: ")
Rev.Reverse_user_name()



