#class introdution
class Dog():
    def __init__(self,breed):
        self.breed = breed

d = Dog('German Sephard')

print(type(d))
print(isinstance(d,Dog))

class Circle():
    def __init__(self,radius=1):
        self.radius = radius
    def area(self):
        area = (3.14*self.radius*self.radius)
        return area
c = Circle(0.3)
print(c.area())
