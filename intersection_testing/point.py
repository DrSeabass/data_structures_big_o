from random import randint

class Point():
    x = None
    y = None

    def __init__(self, x,y) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def intersects(self, point_2, radius : float):
        distance = (self.x - point_2.x) **2 + (self.y - point_2.y)**2
        #sqrt is more pricey than another multiplication
        return distance >= (radius**2)
    
    def random(max_x, max_y):
        return Point(randint(0, max_x), randint(0, max_y))