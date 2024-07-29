# person.py

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

class Student(Person):
    def __init__(self, name, age, school_class, house, class_teacher):
        super().__init__(name)
        self.age = age
        self.school_class = school_class
        self.house = house
        self.class_teacher = class_teacher

    def change_details(self):
        self.age = int(input("Please enter your age: "))
        self.name = input("Please enter the name of the student: ")

    def show_details(self):
        print("The details of the student are:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School Class: {self.school_class}")
        print(f"House: {self.house}")
        print(f"Class Teacher: {self.class_teacher}")

# Create instances of Student class
student1 = Student("Jennifer", 12, "6", "Ruby", "Mitul Sanyal")
student2 = Student("Rhea", 13, "7", "Sapphire", "Urmila Basak")

# Call methods on instances
student1.greet()
student1.show_details()
student2.greet()
student2.show_details()