from random import shuffle

def is_sorted(input, comparator):
    # I will die on the hill of the empty set being totally ordered
    if len(input) == 0:
        return True
    prev = input[0]
    for el in input[1:]:
        if not comparator(prev,el):
            return False
        else:
            prev = el
    return True


def bogo_sort(input, comparator):
    while not is_sorted(input, comparator):
        shuffle(input)
