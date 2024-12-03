class Bucket():
    def __init__(self, key=None):
        self.contents = []
        self.key = key

    def add(self, element):
        raise NotImplemented()
    
    def remove(self, element):
        raise NotImplemented()

class HashTable():

    def __init__(self, hash_function, max_bucket=100):
        self.max_bucket = max_bucket
        self.buckets = []
        for _ in range(self.max_bucket):
            self.buckets.append(Bucket())
        self.hash = hash_function

    def contains(self, element):
        raise NotImplemented()
    
    def retrieve(self, key):
        raise NotImplemented()
    
    def add(self, element):
        raise NotImplemented()



if __name__ == "__main__":
    print("Exercise 3: Hashtables")