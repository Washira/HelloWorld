#Input: รับสตริงหนึ่งบรรทัด
#Process: สร้างสตริงใหม่ที่ทุกอักขระในสตริงที่รับเข้ามาปรากฏซ้ำอีกตัว /n แต่ถ้ามีตัวซ้ำติดกันอยู่แล้วก็ไม่ต้องทำซ้ำ เช่น รับ 'pythonnnaa' จะได้สตริง 'ppyytthhoonnnaa'
#Output: สตริงผลลัพธ์
a= input().strip()
a=" "+a+" "
b=""
for i in range(len(a)-1):
  if a[i]!=a[i+1] and a[i]!=a[i-1]:
    b+=a[i]*2
  else:
    b+=a[i]
  i+=1
print(b)
