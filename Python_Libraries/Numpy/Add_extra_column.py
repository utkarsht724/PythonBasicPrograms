import numpy as np
e=np.array([[10,20,30],[50,60,70]])
print(e)
column_to_be_added=np.array([40,80])
result=np.vstack((e,column_to_be_added))
print( str(result))