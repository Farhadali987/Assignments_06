class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        return f"{self.name} \n {self.marks}"

student_details = Student("Farhad",99)
print(student_details.display())