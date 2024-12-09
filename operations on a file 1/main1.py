file=open('Codingal (1).txt')
print("first line of file")
print(file.readline())
file.close()

file=open('Codingal (1).txt')
print("first three lines of file")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open('Codingal (1).txt')
print("full file")
for line in file:
    print(line)
file.close()