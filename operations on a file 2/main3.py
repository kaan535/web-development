a=open("xyz.txt",'w')
a.write("somthing")
a.close()
import os
os.remove("new.txt")