import os
print("\nEffective Group id: ",os.getegid())
print("Effective user id:",os.geteuid())
print("real group id:",os.getgid())
print("list of supplements group ids:",os.getgroups())





