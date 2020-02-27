import pandas as pd
import numpy as np
from pandas import DataFrame

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
stud_info=pd.DataFrame(exam_data,index=labels)
stud_info.loc['k']=['ut',12,3,'no']
print()
print("After adding a row: ")
print()
print(stud_info)
stud_info.drop('k')
print()
print("After deleting a row: ")
print()
print(stud_info)