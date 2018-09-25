print("Please enter a order number of a month which you want to know about number of date and a B.E. year owns that month (Ex. June in 2550 B.E. please enter to \"6 2550\")")
try:
  m, be = [int(e) for e in input().split()]
  ad = be - 543
  mm = 0
  if 1 <= m <= 12:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
      mm = 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
      mm = 30
    else:
      if (ad % 4 == 0 and ad % 100 != 0) or ad % 400 == 0:
        mm = 29
      else:
        mm = 28
  else:
    print("Your number is not month")
  print("The number date in that month : ", mm)
except ValueError:
  print("Your data is not accepted")
