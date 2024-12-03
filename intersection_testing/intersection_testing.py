from point import Point
from rect import Rect
from space_trees import PointNode, RectNode
        
MAX_X = 640
MAX_Y = 480
SIZES = [1, 10, 25, 50, 100, 1000, 10000]
SAMPLES = 10

# TODO -- Data series generation based on sample size
# TODO -- We need to define division strategies for our trees
# TODO -- Visualiztion tools for points, rectangles, intersection

def test_point_tree():
    results = []
    for size in SIZES:
        print(f"Running w/ {size} points")
        results_at_this_size = []
        for _ in range(SAMPLES):
            points = []
            tree = PointNode(MAX_Y, MAX_X, 0, 0)
            Point.reset_count()
            Rect.reset_count()
            for _ in range(size):
                points.append(Point.random(MAX_X, MAX_Y))
            for point in points:
                tree.add(point)
            for point in points:
                tree.find_intersecting(point, 5.0)
            results_at_this_size.append(Point.test_counts + Rect.test_counts)
        results.append((size, results_at_this_size))
    return results
            

if __name__ == "__main__":
    print("Exercise 2: Intersection Testing")
    values = test_point_tree()
    print(values)