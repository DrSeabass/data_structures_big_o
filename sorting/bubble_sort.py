def bubble_sort(input, comparator):
    sorted_this_pass = False
    while not sorted_this_pass:
        prev = 0
        sorted_this_pass = True
        for i in range(1, len(input)):
            tmp_a = input[prev]
            tmp_b = input[i]
            if not comparator(tmp_a, tmp_b):
                input[prev] = tmp_b
                input[i] = tmp_a
                sorted_this_pass = False
            prev = i