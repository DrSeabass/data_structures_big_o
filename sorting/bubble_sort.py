def bubble_sort(input, comparitor):
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