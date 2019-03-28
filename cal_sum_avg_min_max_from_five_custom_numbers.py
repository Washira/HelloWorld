#choose 5 numbers to this process
number=[]
x=5
i=1
while i <= x:
  print('Number %d:' %i, end='')
  n=int(input())
  number.append(n)
  i+=1
#Calculate summary number
Sum=0
i=1
while i <=x:
  print(number[i-1], end = ', ')
  Sum+= number[i-1]
  i+=1
#Calculate man and min number of them
Min=0
Max=0
i=2
while i<x:
  N=0
  M=0
  if number[i-2]>number[i-1]:
    N=number[i-1]
    M=number[i-2]
  else:
    N=number[i-2]
    M=number[i-1]
  Min=N
  Max=M
  i+=1
#Print all result
print('\nSum = %d' %Sum)
print('Average = %f' %(Sum/x))
print('\nMin = %d' %Min)
print('\nMax = %d' %Max)
