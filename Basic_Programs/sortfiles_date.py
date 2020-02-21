#program to sort files
import glob
import os
files = glob.glob("*.py")
files.sort(key=os.path.getctime)
print("\n".join(files))










