from point import Point

class Rect():
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
    
    def intersects(self, Rect_2) -> bool:
        return (
            # self contains Rect_2
            (self.north >= Rect_2.north and self.south <= Rect_2.south and self.west <= Rect_2.west and self.east >= Rect_2.east) or
            # Rect_2 contains self
            (self.north <= Rect_2.north and self.south >= Rect_2.south and self.west >= Rect_2.west and self.east <= Rect_2.east) or
            # self contains one of the corners of Rect_2 (previous cases handle abutment)
            self.contains(Rect_2.corners[0]) or
            self.contains(Rect_2.corners[1]) or
            self.contains(Rect_2.corners[2]) or
            self.contains(Rect_2.corners[3])
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
        return Rect(north_y, east_x, south_y, west_x)