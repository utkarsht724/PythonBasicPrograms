import time
def sum(a):
    start_time=time.time()
    s=0
    for i in range(1,a+1):
        s=s+i
    end_time=time.time()
    return s,end_time-start_time
print(sum(5))
