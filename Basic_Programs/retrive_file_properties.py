import os.path
import time
print("file:",__file__)
print('access time:',time.ctime(os.path.getmtime(__file__)))
print("Modified time:",time.ctime(os.path.getmtime(__file__)))
print("change time:",time.ctime(os.path.getctime(__file__)))
print("size: ",os.path.getsize(__file__))











