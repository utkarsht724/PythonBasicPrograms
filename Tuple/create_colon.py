#program to colon of a tuple
from copy import deepcopy
tuple=(1,2,[],'xyz')
print(tuple)
tuple_colon = deepcopy(tuple)
tuple_colon[2].append(50)
print(tuple_colon)
print(tuple)