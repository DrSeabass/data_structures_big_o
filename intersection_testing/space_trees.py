from point import Point
from quad import Quad

class SpaceNode(Quad):
    northwest = None
    northeast = None
    southeast = None
    southwest = None
    contained = None
    add_test = None

    def __init__(self, n, e, s, w, add_test=None) -> None:
        super(n,e,s,w)
        self.contained = []
        self.add_test = add_test

    def add(self, el):
        assert(self.add_test(el))
        self.contained.append(el)

    def divide(self) -> list:
        half_width = self.west + (self.east - self.west / 2)
        half_height = self.south + (self.north - self.south)
        self.northwest = PointNode(self.north, half_width, half_height, self.west)
        self.northeast = PointNode(self.north, self.east, half_height, half_width)
        self.southeast = PointNode(half_height, self.east, self.south, half_width)
        self.southwest = PointNode(half_height, half_width, self.south, self.west)

class QuadNode(SpaceNode):

    def __init__(self, n, e, s, w) -> None:
        super(n,e,s,w, self.intersects)

    def __push_children_down(self):
        for quad in self.contained:
            setOne = False
            if self.northwest.contains(quad):
                self.northwest.add(quad)
                setOne = True
            if self.northeast.contains(quad):
                self.northeast.add(quad)
                setOne = True
            if self.southeast.contains(quad):
                self.southeast.add(quad)
                setOne = True
            if self.southwest.contains(quad):
                self.southwest.add(quad)
                setOne = True
            if not setOne:
                raise ValueError("Expected rectangle to intersect at least one sub-quadrant")
        self.contained = None 

    def divide(self) -> list:
        super().divide()
        self.__push_children_down()

class PointNode(SpaceNode):
    northwest = None
    northeast = None
    southeast = None
    southwest = None
    contained = None

    def __init__(self, n, e, s, w) -> None:
        super(n,e,s,w, self.contains)
        self.points = []

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
        super().divide()
        self.__push_children_down()