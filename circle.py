class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

rad = int(input("Enter Radius of Circle"))
aCircle = Circle(rad)
print(aCircle.area())
