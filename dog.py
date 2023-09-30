# dog.py
class Dog:
  # Required properties are defined inside the _init_constructor method
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("dog initialized!")

  # methods are defined as their own named functions inside the class
  # remember to put the "self" parameter every time we make a class method!
  def bark(self):
    print("Woof!")
