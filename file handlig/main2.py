file=open('codingal.txt','r')
print("file in read mode")
print(file.read())
file.close()

file1=open('codingal.txt','w')
file1.write("file in write mode")
file1.write("hello ")
file1.close()

filea=open("codingal.txt",'a')
filea.write("file in append mode")
filea.write("hi")
filea.close()
