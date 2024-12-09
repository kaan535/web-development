file=open('Codingal.txt','r')
print(file.read())
file.close()

file=open('Codingal.txt','r')
print(file.read(10))
file.close()
 
file=open('Codingal.txt','a')
print(file.write("hello"))
file.close()