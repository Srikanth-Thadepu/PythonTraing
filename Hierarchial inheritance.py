class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return 3.14 * self.radius **2

class Square(Shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        return self.side**2
    
def claculate_area(shape):
    return shape.area()

circle=Circle(2)
square=Square(4)

print(claculate_area(circle))
print(claculate_area(square))