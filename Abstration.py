# Student Management System

class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = int(marks)  # Ensure marks are stored as an integer

    def display_info(self):
        print(f"Name : {self.name}, roll_number : {self.roll_number}, marks : {self.marks}")

    def update_marks(self, new_marks):
        self.marks = int(new_marks)  # Ensure new marks are stored as an integer
        print("Marks updated successfully!")

# Creating a Student object
s1 = Student("Karan", "01", "33")  # Marks are passed as a string, but converted to int

# Displaying student information
s1.display_info()

# Updating marks
s1.update_marks(97)

# Display updated information
s1.display_info()
