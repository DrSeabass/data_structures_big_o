from point import Point
from rect import Rect

class SpaceNode(Rect):
    northwest = None
    northeast = None
    southeast = None
    southwest = None
    contained = None
    add_test = None

    def __init__(self, n, e, s, w, add_test=None) -> None:
        super().__init__(n,e,s,w)
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

class RectNode(SpaceNode):

    def __init__(self, n, e, s, w) -> None:
        super().__init__(n,e,s,w, self.intersects)

    def __push_children_down(self):
        for Rect in self.contained:
            setOne = False
            if self.northwest.contains(Rect):
                self.northwest.add(Rect)
                setOne = True
            if self.northeast.contains(Rect):
                self.northeast.add(Rect)
                setOne = True
            if self.southeast.contains(Rect):
                self.southeast.add(Rect)
                setOne = True
            if self.southwest.contains(Rect):
                self.southwest.add(Rect)
                setOne = True
            if not setOne:
                raise ValueError("Expected rectangle to intersect at least one sub-Rectrant")
        self.contained = None 

    def divide(self) -> list:
        super().divide()
        self.__push_children_down()

    def find_intersecting(self, q1 : Rect) -> list:
        to_ret = []
        if self.contained is not None:
            for q2 in self.contained:
                if q2.intersects(q1):
                    to_ret.append(q2)
        else:
            if self.northwest.contains(q1):
                to_ret += self.northwest.find_intersecting(q1)
            if self.southwest.contains(q1):
                to_ret += self.southwest.find_intersecting(q1)
            if self.norteast.contains(q1):
                to_ret += self.northeast.find_intersecting(q1)
            if self.southeast.contains(q1):
                to_ret += self.southeast.find_intersecting(q1)
        return to_ret

class PointNode(SpaceNode):
    northwest = None
    northeast = None
    southeast = None
    southwest = None
    contained = None

    def __init__(self, n, e, s, w) -> None:
        super().__init__(n,e,s,w, self.contains)
        self.points = []

    def __push_children_down(self):
        for point in self.contained:
            if self.northwest.contains(point):
                self.northwest.add(point)
            elif self.northeast.contains(point):
                self.northeast.add(point)
            elif self.southeast.contains(point):
                self.southeast.add(point)
            elif self.southwest.contains(point):
                self.southwest.add(point)
            else:
                raise ValueError("Expected point to be contained in one sub-Rectrant")
        self.contained = None
    
    def divide(self) -> list:
        super().divide()
        self.__push_children_down()

    def find_intersecting(self, p1 : Point, radius=0.) -> list:
        if self.contained is not None:
            to_ret = []
            for p2 in self.contained:
                if p2.intersects(p1,radius):
                    to_ret.append(p2)
            return to_ret
        else:
            if self.northwest.contains(p1):
                return self.northwest.find_intersecting(p1)
            if self.southwest.contains(p1):
                return self.southwest.find_intersecting(p1)
            if self.norteast.contains(p1):
                return self.northeast.find_intersecting(p1)
            if self.southeast.contains(p1):
                return self.southeast.find_intersecting(p1)
