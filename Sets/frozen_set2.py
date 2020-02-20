setA={1,2,3,4,5}
fset= frozenset(setA)
#print(fset)
setA.remove(1)
setA.add(19)
print(fset)