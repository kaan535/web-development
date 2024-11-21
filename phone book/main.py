import sys

def initial_phone_book():
    rows,cols=int(input("Pls enter initial number of contacts")), 5
    phone_book=[]
    print(phone_book)
    for i in range(rows):
        print("\n Enter contact %d details in the following order only"%(i+1))
        print ("note * indicates mandatory feilds")
        print ("..............................................................................................................")
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter name*:")))
                if temp[j]==''or temp[j]==' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j==1:
                temp.append(int(input("enter number*:")))
            if j==2:
                temp.append(str(input("enter email")))
            if j==3:
                temp.append(str(input("enter date of birth(dd/mm/yy)")))
            if j==4:
                temp.append(str(input("enter category(family/freind/work/other)")))
            if temp[j]==''or temp[j]==' ':
                temp[j]=None 
            phone_book.append(temp)
            print(phone_book)
            return phone_book


