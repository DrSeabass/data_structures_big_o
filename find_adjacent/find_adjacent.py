from random import randint
from kd_trees import Node

MAX_DIMM = 3
MAX_VALUE = 100
SAMPLES = 5
SIZE_SCHEDULE = [1, 3, 5, 10, 100, 1000, 10000]

def generate_random_point(max_dimm, max_value):
    ret = []
    for _ in range(max_dimm):
        ret.append(randint(0,max_value))
    return ret

def generate_random_points(samples, max_dimm, max_value):
    ret = []
    for _ in range(samples):
        ret.append(generate_random_point(max_dimm, max_value))
    return ret

def scaling_study():
    to_ret = []
    for size in SIZE_SCHEDULE:
        this_size = []
        for _ in range(SAMPLES):
            this_sample = None
            points = generate_random_points(size, MAX_DIMM, MAX_VALUE)
            tree = Node(MAX_DIMM, points)
            # TODO - instrument tree with counting
            this_size.append(this_sample)
        to_ret.append(this_size)
    return to_ret

if __name__ == "__main__":
    print("Exercise 3b: Nearness in High Dimmensional Space")
    results = scaling_study()
    print(results)