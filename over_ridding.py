# Parent Class
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child Class (Overriding)
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Testing
a = Animal()
d = Dog()
c = Cat()

a.sound()   # Parent class method
d.sound()   # Overridden method in Dog
c.sound()   # Overridden method in Cat
