class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

le = int(input("Enter length"))
wid = int(input("Enter width"))
aRectangle = Rectangle(le,wid)
print (aRectangle.area())

