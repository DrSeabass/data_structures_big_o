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

class Split():
    start = -1
    end = -1
    length = -1

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = self.end - self.start + 1
    
    def split(self):
        if self.length > 1:
            half = self.length // 2
            left = Split(self.start, self.start + half - 1)
            right = Split(self.start + half, self.end)
            return left, right
        else:
            return self, None

    @staticmethod  
    def merge(split_1, split_2, input_list=None, comparitor=None):
        delta = split_2.start - split_1.end
        if delta != 1:
            raise ValueError(f"Splits must be adjacent, {split_1} and {split_2} are not.")
        if input_list is not None:
            index_1 = split_1.start
            index_2 = split_2.start
            # TODO -- do this in place
            merged = []
            while index_2 <= split_2.end and index_1 <= split_1.end:
                if comparitor(input_list[index_1], input_list[index_2]):
                    merged.append(input_list[index_1])
                    index_1 += 1
                else:
                    merged.append(input_list[index_2])
                    index_2 += 1
            for ind in range(index_1, split_1.end+1):
                merged.append(input_list[ind])
            for ind in range(index_2, split_2.end+1):
                merged.append(input_list[ind])
            #print(input_list, split_1, split_2, merged)
            for offset, el in enumerate(merged):
                input_list[split_1.start + offset] = el
        return Split(split_1.start, split_2.end)

    def __len__(self):
        return self.length
    
    def __str__(self):
        return f"[{self.start}, {self.end}]"

def merge_sort(input, split=None, comparitor=default_comparitor):
    if split is None:
        split = Split(0, len(input)-1)
    left, right = split.split()
    if right is None:
        return # base case, single element
    merge_sort(input, split=left, comparitor=comparitor)
    merge_sort(input, split=right, comparitor=comparitor)
    Split.merge(left, right, input_list=input, comparitor=comparitor)
    


def counting_sort(input, radix):
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
    # The other sorts are destructive / in-place
    # Our implementation of counting sort doesn't allow for this
    # We overwrite the original input to get matching destructive behavior
    for i in range(len(input)):
        input[i] = next_list[i]
    

if __name__ == "__main__":
    make_example_inputs()
    print("sorted  :", sorted_data, is_sorted(sorted_data))
    print("reverse :", reversed_order, is_sorted(reversed_order))
    print("shuffled:", shuffled, is_sorted(shuffled))
    print("empty   :", empty, is_sorted(empty))

    merge_sort(shuffled)
    print(shuffled)
