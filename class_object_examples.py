class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.roll_number = None

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, roll_number={self.roll_number})"
        
    def assign_roll_number(self, roll_number):
        self.roll_number = roll_number

# Creating instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1.assign_roll_number(1)
student2.assign_roll_number(2)
print(student1)

# print(student1.roll_number)  # Output: 1
# print(student2.roll_number)   # Output: 2

# id_list = [1, 2, 3, 4, 5]
# id_list.append(6)
# print(id_list)  # Output: [1, 2, 3, 4, 5, 6]

# class List:
#     def __init__(self):
#         self.elements = []
        
#     def append(self, element):
#         self.elements.append(element)
        
#     def __str__(self):
#         return str(self.elements)