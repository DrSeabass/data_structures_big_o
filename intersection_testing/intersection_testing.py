from point import Point
from quad import Quad

class Node(Quad):
    northwest = None
    northeast = None
    southeast = None
    southwest = None
    points = None

    def __init__(self, n, e, s, w) -> None:
        super(n,e,s,w)
        # Leaf nodes may have points
        # Interior nodes only contain quads
        self.points = []
    
    def add(self, p: Point):
        assert(self.contains(p))
        self.points.append(p)

    def __push_children_down(self):
        for point in self.points:
            if self.northwest.contains(point):
                self.northwest.add(point)
            elif self.northeast.contains(point):
                self.northeast.add(point)
            elif self.southeast.contains(point):
                self.southeast.add(point)
            elif self.southwest.contains(point):
                self.southwest.add(point)
            else:
                raise ValueError("Expected point to be contained in one sub-quadrant")
        self.points = None
    
    def divide(self) -> list:
        half_width = self.west + (self.east - self.west / 2)
        half_height = self.south + (self.north - self.south)
        self.northwest = Node(self.north, half_width, half_height, self.west)
        self.northeast = Node(self.north, self.east, half_height, half_width)
        self.southeast = Node(half_height, self.east, self.south, half_width)
        self.southwest = Node(half_height, half_width, self.south, self.west)
        self.__push_children_down()
        

if __name__ == "__main__":
    print("Exercise 2: Intersection Testing")