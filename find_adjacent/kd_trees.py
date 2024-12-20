from math import sqrt, log2, floor

class Node():

    test_count = 0

    def __init__(self, max_axis : int, points : list, depth=0) -> None:
        self.max_axis = max_axis
        self.depth = depth
        self.axis = depth % max_axis
        points.sort(key = lambda el: el[self.axis])
        # To approximate the cost of the sort on the axis
        Node.test_count += floor(log2(len(points)))
        median_index = len(points) // 2
        self.median = points[median_index]
        self.leaf = True
        if median_index != 0:
            self.leaf = False
            self.left = Node(max_axis, points[:median_index],depth+1)
            self.right = Node(max_axis, points[median_index:],depth+1)

    def find_nearest_neightbor(self, point, current_best=None):
        _, current_best_distance = current_best
        dist = self.dimm_distance(self.median, point)
        if self.leaf:
            if current_best is None:
                return (self.median,  dist)
            else:
                if current_best_distance > dist:
                    return (self.median, dist)
                else:
                    return current_best
        else:
            if dist < current_best_distance:
                return self.left.find_nearest_neightbor(point, current_best=(self.median, dist))
            else:
                return self.right.find_nearest_neightbor(point, current_best=current_best)
    
    def dimm_distance(self, point1, point2):
        Node.test_count += 1
        dimm = self.max_axis % self.depth
        return sqrt((point1[dimm] - point2[dimm])**2)
    
    def distance(point1, point2):
        Node.test_count += 1
        sum = 0
        for feat1, feat2 in zip(point1, point2):
            sum += (feat1 - feat2)**2
        return sqrt(sum)
    
    def reset_count():
        Node.test_count = 0
