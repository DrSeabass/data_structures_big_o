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


def radix_sort(input, comparator):
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
