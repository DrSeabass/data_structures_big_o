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