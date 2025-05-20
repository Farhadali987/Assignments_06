class Student:
    def __init__(self,name):
        self.name = name
    
class Teacher(Student):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject

teacher1 = Teacher("Ali","Mathaematices")
print("Name :",teacher1.name)
print("Subject :",teacher1.subject)