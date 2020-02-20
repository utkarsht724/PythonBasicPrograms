import subprocess
returned_txt=subprocess.check_output("dir",shell=True,universal_newlines=True)
print("dir command to list file and directory")
print(returned_txt)












