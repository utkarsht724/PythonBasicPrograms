#poggram to  print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def dic():
    n=int(input("enter a range:"))
    for key in range(1,n):
        dictionary={key:key*key}
        print(dictionary)
dic()
