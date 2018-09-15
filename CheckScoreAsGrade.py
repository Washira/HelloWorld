score = float(input("Enter score :"))
if 80<=score<=100:
  print("Grade :"+"A")
elif 75<=score<80:
  print("Grade :"+"B+")
elif 70<=score<75:
  print("Grade :"+"B")
elif 60<=score<75:
  print("Grade :"+"C")
elif 55<=score<60:
  print("Grade :"+"D+")
elif 50<=score<55:
  print("Grade :"+"D")
elif 0<=score<50:
  print("Grade :"+"F")
else:
  print("ERROR")
