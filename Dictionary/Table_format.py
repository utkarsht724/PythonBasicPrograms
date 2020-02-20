#program to print dictionary in table format
A={"name":"XYZ","SEX":"MALE","AGE":22}
for row in zip(*(key+(value) for key,value in sorted(A.items()))):
    print(*row)