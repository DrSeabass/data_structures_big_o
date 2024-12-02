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
    

def merge_sort(input, comparitor, split=None):
    if split is None:
        split = Split(0, len(input)-1)
    left, right = split.split()
    if right is None:
        return # base case, single element
    merge_sort(input, comparitor, split=left)
    merge_sort(input, comparitor, split=right, )
    Split.merge(left, right, input_list=input, comparitor=comparitor)