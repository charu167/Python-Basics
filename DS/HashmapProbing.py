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
        h = self.Hash(key)
        if self.arr[h] == None:
            self.arr[h] = [key, value]
        elif key == self.arr[h][0]:
            self.arr[h][1] = value
        else:
            while self.arr[h] != None:
                h+=1
            self.arr[h] = [key, value]

        



    def __getitem__(self, key):
        h = self.Hash(key)
        if self.arr[h] != None:
            if self.arr[h][0] == key:
                return self.arr[h]
            else:
                while self.arr[h][0] != key:
                    if self.arr[h+1][0] == key:
                        return self.arr[h+1]
                    elif h+1>=len(self.arr):
                        break
                    h+=1 
                if self.Hash(key) != 0:
                    h=0
                    while self.arr[h][0] != key:
                        if self.arr[h+1][0] == key:
                            print('###############')
                            return self.arr[h+1]
                        elif h+1 >= self.Hash(key):
                            break
                        h+=1
        else:
            return 'No records found'
        
    def __delitem__(self, key):
        self.arr[self.Hash(key)] = None


h = HashTable(10)

h['Aditi'] = 1
h['Ashish'] = 2
h['Akriti'] = 3
h['Atharv'] = 4
h['Aditya'] = 5
h['SP'] = 6

for i in ['Aditi', 'Ashish', 'Akriti', 'Atharv', 'Aditya', 'SP']:
    print(h.Hash(i), end=" ")

print('\n',h.arr)
print(h['Aditya'])