def notes(a):
    Q=[2000,500,200,100,50,20,10,1]
    x=0
    for i in range(8):
        q = Q[i]
        x=a//q
        print ("notes of {}={}".format(q,x))
        a = a%q

amount=int(input("Enter amount"))
notes(amount)
    