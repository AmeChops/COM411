#the class (kinda like a blueprint)
class Person:

  #class attributes
  #constant (once initial value assigned, does not change)
  MAX_ENERGY = 100
  MIN_ENERGY = 1


  #initialiser (special instance method)
  def __init__(self, name, age, height = 0, weight = 0):

    #instance attributes
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight
    self.energy = Person.MAX_ENERGY

  def grow(self):
    self.age += 1

  def display(self):
    print(f"My name is {self.name} and I am {self.age} years old and my energy is {self.MAX_ENERGY}")

#the object
if (__name__ = "__main__"):
  darren = Person("Darren", 18, 180)
  darren.display()
  darren.grow()
  darren.display()
