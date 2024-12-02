from random import shuffle

DEFAULT_SIZE = 10
sorted_data = None
reversed_order = None
shuffled = None


def make_example_inputs():
    global sorted_data, reversed_order, shuffled
    sorted_data = list(range(DEFAULT_SIZE))
    reversed_order = sorted_data.copy()
    shuffled = sorted_data.copy()
    reversed_order.reverse()
    shuffle(shuffled)
    

if __name__ == "__main__":
    make_example_inputs()
    print("sorted  :", sorted_data)
    print("reverse :", reversed_order)
    print("shuffled:", shuffled)
    