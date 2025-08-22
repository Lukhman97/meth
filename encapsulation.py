class Student:
    def __init__(self, name, age, marks):
        self.name = name          # Public
        self._age = age           # Protected
        self.__marks = marks      # Private

    # Getter for private variable
    def get_marks(self):
        return self.__marks

    # Setter for private variable
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")

# Create object
s1 = Student("Rahul", 20, 85)

# Public → Accessible directly
print("Name:", s1.name)  

# Protected → Accessible, but should be used carefully
print("Age:", s1._age)   

# Private → ❌ Not accessible directly
# print(s1.__marks)  # Error

# Access private using getter & setter
print("Marks:", s1.get_marks())  

s1.set_marks(95)  
print("Updated Marks:", s1.get_marks())






