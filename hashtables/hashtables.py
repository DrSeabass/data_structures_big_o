from container import Container

class Bucket():
    test_counts = 0
    def __init__(self):
        self.contents = []

    def add(self, key, element):
        self.contents.append(Container(key, element))
    
    def remove(self, key, element):
        new_contents = []
        deleted_count = 0
        for container in self.contents:
            Bucket.test_counts += 1
            if container.key != key or container.element != element:
                new_contents.append(container)
            else:
                deleted_count += 1
        assert(deleted_count < 2)
        return deleted_count
    
    def find(self, key):
        for container in self.contents:
            Bucket.test_counts += 1
            if container.key == key:
                return container.element
        return None

    def contains(self, key):
        return self.find(key) is not None
    
    def reset_count():
        Bucket.test_counts = 0

class HashTable():
    test_count = 0

    def __init__(self, hash_function, max_bucket=100):
        self.max_bucket = max_bucket
        self.buckets = []
        for _ in range(self.max_bucket):
            self.buckets.append(Bucket())
        self.hash = hash_function

    def contains(self, key):
        HashTable.test_count += 1
        bucket = self.buckets[key % self.max_bucket]
        return bucket.contains(key)
    
    def retrieve(self, key):
        HashTable.test_count += 1
        bucket = self.buckets[key % self.max_bucket]
        return bucket.find(key)
    
    def add(self, element, key=None):
        HashTable.test_count += 1
        if key is None:
            key = self.hash(element)
        bucket = self.buckets[key % self.max_bucket]
        bucket.add(key, element)
        return key

    def remove(self, element):
        HashTable.test_count += 1
        key = self.hash(element)
        bucket = self.buckets[key % self.max_bucket]
        bucket.remove(key, element)

    def extend(self):
        new_max = self.max_bucket * 2
        new_buckets = []
        for i in range(new_max):
            new_buckets.append(Bucket())
        for bucket in self.buckets:
            for container in bucket.contents:
                # We can end-run the insertion function because we already have the wrapped object
                HashTable.test_count += 1
                new_buckets[container.key % new_max].contents.append(container)
        self.buckets = new_buckets

    def reset_count():
        HashTable.test_count = 0


if __name__ == "__main__":
    print("Exercise 3: Hashtables")