#Overriding practice
class bird:
  def __init__(self,name):
    self.name = name
  def fly(self):
    print("%s flying!!!" %self.name)

class chicken(bird):
  def __init__(self,name,sex,age):
    self.name = name
    self.sex = sex
    self.age = age
  def fly(self):
    print("%s can not fly" %self.name) 

class eagle(bird):
  def __init__(self,name,family):
    self.name = name
    self.family = family
  def fly(self):
    print("%s is able to high speed flyyyyyy" %self.name)

#create instance
bird1 = bird("Nok")
bird1.fly()
bird2 = chicken("Jeab","male",1)
print("I'm ", bird2.name, "and I'm too young because I'm only ", bird2.age, "year old.")
bird2.fly()
bird3 = eagle("Albatros","White eagle")
print("Hi, I'm", bird3.name)
bird3.fly()
