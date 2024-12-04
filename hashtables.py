class Container():
    def __init__(self, key, element):
        self.key = key
        self.element = element

class Bucket():
    def __init__(self):
        self.contents = []

    def add(self, key, element):
        self.contents.append(Container(key, element))
    
    def remove(self, key, element):
        new_contents = []
        deleted_count = 0
        for container in self.contents:
            if container.key != key or container.element != element:
                new_contents.append(container)
            else:
                deleted_count += 1
        return deleted_count
    
    def find(self, key):
        for container in self.contents:
            if container.key == key:
                return container.element
        return None

    def contains(self, key):
        return self.find(key) is not None

class HashTable():

    def __init__(self, hash_function, max_bucket=100):
        self.max_bucket = max_bucket
        self.buckets = []
        for _ in range(self.max_bucket):
            self.buckets.append(Bucket())
        self.hash = hash_function

    def contains(self, key):
        bucket = self.buckets[key % self.max_bucket]
        return bucket.contains(key)
    
    def retrieve(self, key):
        bucket = self.buckets[key % self.max_bucket]
        return bucket.find(key)
    
    def add(self, element, key=None):
        if key is None:
            key = self.hash(element)
        bucket = self.buckets[key % self.max_bucket]
        bucket.add(key, element)

    def remove(self, element):
        key = self.hash(element)
        bucket = self.buckets[key % self.max_bucket]
        bucket.remove(key, element)

    def extend(self):
        raise NotImplemented()



if __name__ == "__main__":
    print("Exercise 3: Hashtables")