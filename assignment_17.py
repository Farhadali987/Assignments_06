def add_greeting(cls):

    def greet(self):
        return "Hello from Decorator"
    
    setattr(cls,"greet",greet)
    return cls

@add_greeting
class Person:
    def __init__(self,name):
        self.name = name

p = Person("Ali")
print(p.greet())