from os import listdir
from os.path import isfile ,join
files_list = [f for f in listdir('/home/PythonBasicPrograms') if isfile(join('/home/Python/BasciPrograms', f))]
print(files_list)