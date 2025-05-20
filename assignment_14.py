class Employee:
    
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id

class Department:

    def __init__(self,dept_name,employee):
        self.dept_name = dept_name
        self.employee = employee

emp = Employee("Naveed",101)
dept = Department("Hr",emp)
print(dept.employee.name)
print(dept.employee.emp_id)