from random import shuffle, randint

DEFAULT_SIZE = 10
MAX_INT = 10000
MIN_INT = 0
sorted_data = None
reversed_order = None
shuffled = None
empty = []
random_values = []


def default_comparitor(a,b):
    return a < b


def make_example_inputs():
    global sorted_data, reversed_order, shuffled
    sorted_data = list(range(DEFAULT_SIZE))
    reversed_order = sorted_data.copy()
    shuffled = sorted_data.copy()
    reversed_order.reverse()
    shuffle(shuffled)
    for i in range(DEFAULT_SIZE):
        random_values.append(randint(MIN_INT, MAX_INT))

    
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
    while not is_sorted(input):
        shuffle(input)


def bubble_sort(input, comparitor=default_comparitor):
    items = len(input)
    if items == 0:
        return
    sorted_this_pass = False
    while not sorted_this_pass:
        prev = 0
        sorted_this_pass = True
        for i in range(1, items):
            tmp_a = input[prev]
            tmp_b = input[i]
            if not comparitor(tmp_a, tmp_b):
                input[prev] = tmp_b
                input[i] = tmp_a
                sorted_this_pass = False
            prev = i


def merge_sort(input, comparitor=default_comparitor):
    raise NotImplemented


def counting_sort(input, radix):
    # TODO / NOTE: This sort is non-destructive (the rest are!)
    buckets = [[], [], [], [], [], [], [], [], [], [],] # one for each digit in 0 - 9
    # Bucketize input based on radix
    saw_non_zero = False
    for el in input:
        bucket = el % (radix * 10) // radix
        saw_non_zero = saw_non_zero or bucket > 0
        buckets[bucket].append(el)
    
    # reconstruct output from buckets
    output = []
    for bucket in buckets:
        output.extend(bucket)
    return output, saw_non_zero


def radix_sort(input):
    radix = 1
    finished = False
    next_list = input
    while not finished:
        next_list, saw_non_zero = counting_sort(next_list, radix)
        radix *= 10
        finished = not saw_non_zero
    return next_list
    

if __name__ == "__main__":
    make_example_inputs()
    print("sorted  :", sorted_data, is_sorted(sorted_data))
    print("reverse :", reversed_order, is_sorted(reversed_order))
    print("shuffled:", shuffled, is_sorted(shuffled))
    print("empty   :", empty, is_sorted(empty))
