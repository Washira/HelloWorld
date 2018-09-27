def g(m):
  i=1
  for i in range(m):
    print(" "*(m),"*"*i)
    i+=1
    m-=1
  j=0
  for j in range(i):
    print(" "*(j),"*"*i)
    j+=1
    i-=1
a = int(input("How many size do you want?:"))
#Please considering about matching size program window
g(a)
