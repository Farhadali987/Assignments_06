class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Farhd","382983","123-389283")
print(emp.name)
print(emp._salary)
print(emp.__ssn)