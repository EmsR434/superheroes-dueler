
class Animal:
    def __init__(self, name, sleep_duration, eat, drink):
        self.name = name
        self.sleep_time = sleep_duration

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

    def sleep(self):
        print(f"{self.name} sleeps for hours {self.sleep_time}")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping")
# note that the class dog takes in Animal as a perimeter!
class Dog(Animal):
    def bark(self):
        print("Woof! Woof")


dog = Animal("sophie", 12)
dog.sleep()