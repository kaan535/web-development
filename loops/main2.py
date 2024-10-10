num=27
flag=False

if num>1:
  for i in range(2,num):
    if(num%i)==0:
      flag=True
      break
if flag==True:
  print("not a prime number")
else:
  print("is a prime number")