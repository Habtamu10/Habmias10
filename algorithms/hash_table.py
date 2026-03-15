# Custom Hash Table / HashMap in Python
class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        self.table[index] = [p for p in self.table[index] if p[0] != key]

hm = HashMap()
hm.put("name", "Habtamu")
hm.put("role", "Engineer")
print(hm.get("name"))  # Habtamu
hm.remove("name")
print(hm.get("name"))  # None
