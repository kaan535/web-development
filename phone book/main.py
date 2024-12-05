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
                temp.append(str(input("enter category(family/freind/work/others)")))
            if temp[j]==''or temp[j]==' ':
                temp[j]=None 
            phone_book.append(temp)
            print(phone_book)
            return phone_book

def menu();
print("***********************************************************************************************************************")
print("\t\tsmartphone directory",flush=False)
print("***********************************************************************************************************************")
print("\tyou can now perform the following actions\n")
print("1:add a new contact")
print("2:remove an existing contact")
print("3:delete all contacts")
print("4:search for a contact")
print("5:display all contacts")
print("6:exit phone book")
choice = int(input("please enter your choice"))

def add_contact(pb):
    dip =[]
    for i in range(len(pb[0])):
      if i == 0:
        dip.append(str(input("enter name:")))
      if i == 1:
        dip.append(int(input("enter number:")))
      if i == 2:
        dip.append(str(input("enter e-mail address:")))
      if i == 3:
        dip.append(str(input("enter date of birth")))
      if i == 4:
        dip.append(
        str(input("enter category(family/freinds/work/others):")))
    pb.append(dip)
    return pb
def remove_existing(pb):
    query = str
    (input ("please enter the name of the conatact you wish to remove:"))
    temp=0
    for i in range(len(pb)):
        if query ==pb[i][0]:
            temp += 0
            print (pb.pop(i))
            print("this query has now been removed")
            return pb
    if temp ==0:
     print("sorry you have entered an invalid query")
def delete_all(pb):
    return pb.clear()
def search_existing(pb):
    choice=int(iput("enter search 1,2,3,4, or 5 (1=name 2=number 3=email 4=date of birth 5=contact)"))
    temp=[]
    check = -1

    if choice ==1:
        query=str(input("please enter name of the contact"))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check=i
                temp.append(pb[i])
            
    elif choice ==2:
        query=str(input("please enter number of the contact"))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check=i
                temp.append(pb[i])
    
    elif choice ==3:
        query=str(input("please enter e-mail of the contact"))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check=i
                temp.append(pb[i])
    elif choice ==4:
        query=str(input("please enter the date of birth of the contact"))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check=i
                temp.append(pb[i])
    elif choice ==5:
        query=str(input("please enter category of the contact(family/freinds/work/others)"))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check=i
                temp.append(pb[i])
    else:
        print("invalid search criteria")
        return -1
    
    if check == -1:
        return -1
    else:
        display_all(temp)
        return check

def display_all(pb):
         if not pb:
        else:
            for i in range