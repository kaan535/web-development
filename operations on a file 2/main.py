with open('Codingal (1).txt','w')as file:
    file.write("hello i am kaan i am 10.9 years old")
file.close()

with open('Codingal(1).txt','r')as file:
    data=file.readlines()
    print("words in this file are........")
    for line in data:
        word = line.split()
        print(word)
file.close()

