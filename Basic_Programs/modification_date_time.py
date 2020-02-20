import os.path,time
print("last modified:%s"%time.ctime(os.path.getmtime('modification_date_time.py')))
print("created:%s"%time.ctime(os.path.getctime('modification_date_time.py')))