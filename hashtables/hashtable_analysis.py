from math import floor
from random import shuffle

from bucket import Bucket
from hashtable import HashTable

SIZE_SCHEDULE = [1, 10, 100, 1000, 10000]
HASH_SCHEDULE = [ 0, 0.1, 0.25, 0.5, 0.75, 0.95 ]
SAMPLES = 5

def make_hash(max_int, collision_rate):
    if collision_rate == 0:
        return lambda value : value
    modulus = max_int - floor(float(max_int) * collision_rate)
    return lambda value: value % modulus

def scaling_study_no_extension():
    results = []
    for collision_rate in HASH_SCHEDULE:
        these_results = []
        for size in SIZE_SCHEDULE:
            size_results = []
            for _ in range(SAMPLES):
                Bucket.reset_count()
                HashTable.reset_count()
                hash_fn = make_hash(size, collision_rate)
                hash_table = HashTable(hash_fn, max_bucket=size)
                data = list(range(1,size))
                shuffle(data)
                # Put it all in
                for datum in data:
                    hash_table.add(datum)
                shuffle(data)
                # Take it all out
                for datum in data:
                    hash_table.remove(datum)
                size_results.append(Bucket.test_count + HashTable.test_count)
            these_results.append(size_results)
        results.append(these_results)
    return results


if __name__ == "__main__":
    print("Exercise 3: Hashtables")
    results = scaling_study_no_extension()
    print(results)