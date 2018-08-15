#Reading the number in Thai language
#Enter number 0 - 999999 (6 digits)
print("Please enter your numerical value between 0-999999:")
try:
  num = input()
  #defines exception at argument number of num is greater than 6
  if len(num) > 6:
    raise Exception("Your number is not allowed here!")
  #contains parameters of num in list x
  x = [e for e in num]
  #creates variables and contains each number from x
  a = 0
  if len(x) <6:
    a = 0
  else:
    a = int(x[-6])
  b = 0
  if len(x) <5:
    b = 0
  else:
    b = int(x[-5])
  c = 0
  if len(x) <4:
    c = 0
  else:
    c = int(x[-4])
  d = 0
  if len(x) <3:
    d = 0
  else:
    d = int(x[-3])
  e = 0
  if len(x) <2:
    e = 0
  else:
    e = int(x[-2])
  f = 0
  if len(x) <1:
    f = 0
  else:
    f = int(x[-1])
  #contains a, b, c, d, e, f in list x1
  x1 = [a, b, c, d, e, f]
  #creates 2 lists to deploy Thai words
  base = ["แสน", "หมื่น", "พัน", "ร้อย", "สิบ", ""]
  name = \
  ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
  #creates another set of variables to contain Thai words deploying from list x1
  aa, bb, cc, dd, ee, ff = "", "", "", "", "", ""
  if a > 0:
    aa = name[a] + base[0]
  else:
    aa = ""
  if b > 0:
    bb = name[b] + base[1]
  else:
    bb = ""
  if c > 0:
    cc = name[c] + base[2]
  else:
    cc = ""
  if d > 0:
    dd = name[d] + base[3]
  else:
    dd = ""
  if e > 0:
    ee = name[e] + base[4]
    if e == 2:
      ee = "ยี่" + base[4]
    if e == 1:
      ee = "" + base[4]
  else:
    ee = ""
  if f > 0:
    ff = name[f] + base[5]
    if f == 1:
      if a or b or c or d or e != 0:
        ff = "เอ็ด" + base[5]
  elif f == 0:
    if a == 0:
      if b == 0:
        if c == 0:
          if d == 0:
            if e == 0:
              ff = "ศูนย์" + base[5]
  else:
    ff = ""
  #creates list y to contain variables
  y = [aa, bb, cc, dd, ee, ff]
  yy = "".join(e for e in y)
  print("Read the number in Thai:", yy)
  #creates exception for except value error
except ValueError as e:
  print("Your value is not numeric!!!")
