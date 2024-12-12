import os
print("checking if file exists or not.....")
if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("file does not exist")

