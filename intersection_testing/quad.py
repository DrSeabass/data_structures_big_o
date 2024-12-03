from point import Point

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
    
    def random(max_x, max_y):
        c1 = Point.random(max_x, max_y)
        c2 = Point.random(max_x, max_y)
        c3 = Point.random(max_x, max_y)
        c4 = Point.random(max_x, max_y)
        west_x = min(c1.x, c2.x, c3.x, c4.x)
        east_x = max(c1.x, c2.x, c3.x, c4.x)
        south_y = min(c1.y, c2.y, c3.y, c4.y)
        north_y = max(c1.y, c2.y, c3.y, c4.y)
        return Quad(north_y, east_x, south_y, west_x)