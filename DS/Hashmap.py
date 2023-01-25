class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = []
        for i in range(0,size):
            self.arr.append(None)

    def Hash(self, key):
        h = 0
        for i in key:
            h+=ord(i)
        return h%self.size

    def insert(self, key, value):
        self.arr[self.Hash(key)] = value

    def get(self, key):
        if self.arr[self.Hash(key)] != None:
            return self.arr[self.Hash(key)]
        else:
            return 'No records found'
        
    def delete(self, key):
        self.arr[self.Hash(key)] = None


h = HashTable(100)
h.insert('Aditi', 1)
h.insert('Ashish', 2)
h.insert('Akriti', 3)
h.insert('Atharv', 4)

print(h.get('Atharv'))