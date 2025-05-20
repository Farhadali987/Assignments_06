from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,hieght):
        self.width = width
        self.hieght = hieght
    
    def area(self):
        return self.width * self.hieght

rect = Rectangle(4,5)
print(rect.area())