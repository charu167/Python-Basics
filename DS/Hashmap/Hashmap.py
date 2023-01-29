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

    def __setitem__(self, key, value):
        self.arr[self.Hash(key)] = value

    def __getitem__(self, key):
        if self.arr[self.Hash(key)] != None:
            return self.arr[self.Hash(key)]
        else:
            return 'No records found'
        
    def __delitem__(self, key):
        self.arr[self.Hash(key)] = None


h = HashTable(100)

h['Aditi'] = 1
h['Ashish'] = 2
h['Akriti'] = 3
h['Atharv'] = 4


print(h['Atharv'])