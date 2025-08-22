# ----single level-----
# ---A child class inherits from only one parent class.


class Parent:
    def display(self):
        print("This is Parent class")

class Child(Parent):   
    def show(self):
        print("This is Child class")

obj = Child()
obj.display()
obj.show()

# -----multilevel inhertance---
# -----A child class inherits from more than one parent class


class Father:
    def skill(self):
        print("Father: Knows driving")

class Mother:
    def skill(self):
        print("Mother: Knows cooking")

class Child(Father, Mother):  
    def talent(self):
        print("Child: Plays football")

obj = Child()
obj.skill()   
obj.talent()


# --------Multilevel Inheritance------
# -more chain two genrations inherits


class Grandparent:
    def house(self):
        print("Grandparent: Owns a house")

class Parent(Grandparent):
    def car(self):
        print("Parent: Owns a car")

class Child(Parent):
    def bike(self):
        print("Child: Owns a bike")

obj = Child()
obj.house()
obj.car()
obj.bike()

# ------Hierarchical Inheritance
# ----Multiple child classes inherit from the same parent class.

class Parent:
    def property(self):
        print("Parent: Owns land")

class Child1(Parent):
    def house(self):
        print("Child1: Owns a house")

class Child2(Parent):
    def car(self):
        print("Child2: Owns a car")

obj1 = Child1()
obj1.property()
obj1.house()

obj2 = Child2()
obj2.property()
obj2.car()

# ----Hybrid Inheritance
# ---Combination of two or more types of inheritance.


class A:
    def featureA(self):
        print("Feature of A")

class B(A):
    def featureB(self):
        print("Feature of B")

class C(A):
    def featureC(self):
        print("Feature of C")

class D(B, C):   
    def featureD(self):
        print("Feature of D")

obj = D()
obj.featureA()   
obj.featureB()   
obj.featureC()   
obj.featureD()  
