#Parking fee
#parking open 7:00 - 23:00
#park within 15 min --> free charge
#park to not over than 3 hrs. --> 10 Bht per hr.
#park to not over than 6 hrs. --> 20 Bht per hr.
#park from 6 hrs. up --> 200 Bht (package all the day) 
# minute remainder is charged to one hr.
try:
  inHr = int(input("Enter the parking start time (hr) :")) 
  inMn = int(input("Enter the parking start time (min) :"))
  outHr = int(input("Enter the parking finished time (hr) :"))
  outMn = int(input("Enter the parking finished time (min) :"))
  if inHr < 7 or outHr > 23:
    print("Out of service!!!")
  else:
    dH = outHr - inHr
    dM = outMn - inMn
    fee = 0
    if dH == 0 and dM <= 15:
      fee = 0
    elif 0 <= dH < 3:
      if dM==0:
        fee = 10*dH
      else:
        fee = 10*dH + 10
    elif dH == 3:
      if dM > 0:
        fee = 50
      else:
        fee = 30
    elif 3 < dH < 6:
      if dM== 0:
        fee == 200
      else:
        fee = 10*dH + 20
    elif dH == 6:
      if dM > 0:
        fee = 200
      else:
        fee = 120
    else:
      fee = 200
    print()
    print("Please take your cash :", fee, "Baht")
except ValueError:
  print("No enter string allowed!!!")
