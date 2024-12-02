from random import shuffle

DEFAULT_SIZE = 10
sorted_data = None
reversed_order = None
shuffled = None
empty = []


def default_comparitor(a,b):
    return a < b


def make_example_inputs():
    global sorted_data, reversed_order, shuffled
    sorted_data = list(range(DEFAULT_SIZE))
    reversed_order = sorted_data.copy()
    shuffled = sorted_data.copy()
    reversed_order.reverse()
    shuffle(shuffled)

    
def is_sorted(input, comparitor=default_comparitor):
    # I will die on the hill of the empty set being totally ordered
    if len(input) == 0:
        return True
    prev = input[0]
    for el in input[1:]:
        if not comparitor(prev,el):
            return False
        else:
            prev = el
    return True


def bogo_sort(input, comparitor=default_comparitor):
    raise NotImplemented


def bubble_sort(input, comparitor=default_comparitor):
    raise NotImplemented


def merge_sort(input, comparitor=default_comparitor):
    raise NotImplemented


def radix_sort(input, comparitor=default_comparitor):
    raise NotImplemented
    

if __name__ == "__main__":
    make_example_inputs()
    print("sorted  :", sorted_data, is_sorted(sorted_data))
    print("reverse :", reversed_order, is_sorted(reversed_order))
    print("shuffled:", shuffled, is_sorted(shuffled))
    print("empty   :", empty, is_sorted(empty))
