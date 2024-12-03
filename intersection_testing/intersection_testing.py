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
    
class Quad():
    north = None
    east = None
    south = None
    west = None
    corners = None

    def __init__(self, n, e, s, w):
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        self.corners = [Point(n,w), Point(n,e), Point(s,e), Point(s,w)]

    def __str__(self):
        return f"[({self.west}, {self.north}), ({self.east}, {self.north}), ({self.east}, {self.south}), ({self.west}, {self.south})]"
    
    def contains(self, p : Point) -> bool:
        return (
            p.x >= self.west and
            p.x <= self.east and
            p.y >= self.south and
            p.y <= self.north
        )
    
    def intersects(self, quad_2) -> bool:
        return (
            # self contains quad_2
            (self.north >= quad_2.north and self.south <= quad_2.south and self.west <= quad_2.west and self.east >= quad_2.east) or
            # quad_2 contains self
            (self.north <= quad_2.north and self.south >= quad_2.south and self.west >= quad_2.west and self.east <= quad_2.east) or
            # self contains one of the corners of quad_2 (previous cases handle abutment)
            self.contains(quad_2.corners[0]) or
            self.contains(quad_2.corners[1]) or
            self.contains(quad_2.corners[2]) or
            self.contains(quad_2.corners[3])
        )


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