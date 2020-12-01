class Human:

  # A class attribute
  MAX_ENERGY = 100

  # A class method
  def energy():
    print(f"My maximum energy is {Human.MAX_ENERGY}")

  # An initialiser (special instance method)
  def __init__(self):

    # An instance attribute
    self.name = "Human"
    self.age = 0
    self.energy = Human.MAX_ENERGY

  # An instance method
  def display(self):
    print(f"I am {self.name}")

if (__name__ == "__main__"):
  human = Human()
  human.display()
  Human.energy()