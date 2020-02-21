def leading_zero():
    str=" 22.455"
    print("original string",str)
    str=str.ljust(12,'0')
    print(str)
    str=str.ljust(50,'0')
    print(str)
leading_zero()