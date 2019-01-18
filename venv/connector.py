import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



class Person:
  def __init__(self, name, age):         #Using definition
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)