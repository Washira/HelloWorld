#check even or odd number of integer
n=int(input("Enter a number:"))
if n>0:
  if n%2==0: 
    print("%d is even number!" %n)
  else: 
    print("%d is odd number!" %n)
elif n<0:
  if n%2==0: 
    print("%d is even minus number!" %n)
  else: 
    print("%d is odd minus number!" %n)
else: print("%f is zero!" %n)
