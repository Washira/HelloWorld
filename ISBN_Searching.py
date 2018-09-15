#Enter ISBN No. for 9 digits and keep in isbn var
isbn = input("Enter ISBN number 1-9 digits:")
#transform isbn to list "num"
num = [int(e) for e in isbn] 
i, x, s = 0, 10, 0
#take 10(1)+9(2)+8(3)+...+2(9) equal sum "s"
while i < len(num): 
  num[i] = num[i]*x
  s += num[i]
  x -= 1
  i += 1
#Find n10 that makes (s=n10)%11==0
n = 11 - (s % 11)
n10 = 0
#Ensure that n10 is not 10 (n10 is the last digit of isbn)
if n == 10:
  n10 = n - 9
else:
  n10 = n
#show output that is isbn (9 digits) and n10 is the last digit filling to isbm
print("Your ISBN:", isbn + str(n10))
