from random import shuffle, randint
from bogo_sort import is_sorted, bogo_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from radix_sort import radix_sort

DEFAULT_SIZE = 10
MAX_INT = 10000
MIN_INT = 0
sorted_data = None
reversed_order = None
shuffled = None
empty = []
random_values = None
comparison_calls = 0


def default_comparator(a,b):
    global comparison_calls
    comparison_calls += 1
    return a < b


def reset_counter():
    global comparison_calls
    comparison_calls = 0


def make_random_input(size=DEFAULT_SIZE, samples=5):
    ret = []
    for _ in range(samples):
        this_list = []
        for _ in range(size):
            this_list.append(randint(MIN_INT, MAX_INT))
        ret.append(this_list)
    return ret


def make_example_inputs():
    global sorted_data, reversed_order, shuffled, random_values
    sorted_data = list(range(DEFAULT_SIZE))
    reversed_order = sorted_data.copy()
    shuffled = sorted_data.copy()
    reversed_order.reverse()
    shuffle(shuffled)
    random_values = make_random_input(samples=1)[0]


if __name__ == "__main__":
    make_example_inputs()
    print("sorted  :", sorted_data, is_sorted(sorted_data, default_comparator))
    print("reverse :", reversed_order, is_sorted(reversed_order, default_comparator))
    print("shuffled:", shuffled, is_sorted(shuffled, default_comparator))
    print("empty   :", empty, is_sorted(empty, default_comparator))
    reset_counter()

    print(random_values)
    #bogo_sort(random_values, default_comparator)
    #bubble_sort(random_values, default_comparator)
    #radix_sort(random_values)
    #merge_sort(random_values, default_comparator)
    print(random_values)