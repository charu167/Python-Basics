#Hashmap Chaining --> insert, get, update, delete

class Hashmap:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for i in range(self.size)]
    def Hash(self, key):
        h = 0
        for i in key:
            h+=ord(i)
        return h%self.size

    def __setitem__(self, key, value):
        h = self.Hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found  = True
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.Hash(key)
        for i in self.arr[h]:
            if i[0] == key:
                return i[1]

    def __delitem__(self, key):
        h = self.Hash(key)
        for i, e in enumerate(self.arr[h]):
            if e[0] == key:
                del self.arr[h][i]



h= Hashmap(6)


h['Aditi'] = 1
h['Akriti'] = 2
h['Ashish'] = 3
h['SP'] = 4
h['Atharv'] = 5
h['Badakh'] = 6

print(h.Hash('Aditi'))
print(h.arr)

#[[None], [None], [None], [None], [None], [None], [None], [None], [None], [None]]