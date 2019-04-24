import hashlib

class hashMap:

    def __init__(self):
        self.length = 0
        self.hashMap = [None] * 255

    def add(self, key, value):
        hashkey = hashMap.__gethash__(key)
        if not self.hashMap[hashkey]:
            self.hashMap.insert(hashkey, [key, value])
            self.length += 1
        elif self.hashMap[hashkey][0] != key:
            self.hashMap[hashkey].append(key)
            self.hashMap[hashkey].append(value)
            self.length += 1
        else:
            self.hashMap[hashkey][1] = value

    def get(self, key):
        hashkey = hashMap.__gethash__(key)
        if self.hashMap[hashkey]:
            if len(self.hashMap[hashkey]) == 2:
                return self.hashMap[hashkey][1]
            elif len(self.hashMap[hashkey]) > 2:
                idx = self.__find_if_hashclash__(hashkey, 'v')
                return self.hashMap[hashkey][idx]
        else:
            return None

    def remove(self, key):
        theKey = hashMap.__gethash__(key)
        if self.hashMap[theKey]:
            if len(self.hashMap[theKey]) == 2:
                self.hashMap[hashMap.__gethash__(key)] == None
            else:
                hashkey = hashMap.__gethash__(key)
                idx = self.__find_if_hashclash__(hashkey, 'i')
                self.hashMap[hashkey].pop(idx)
                self.hashMap[hashkey].pop(idx+1)
            self.length -= 1


    def size(self):
        return self.length

    def containsKey(self):
        #Only do if the rest is done
        #handle hashclash by iterating through list
        # find key.  value will be key idx + 1
        pass

    def __find_if_hashclash__(self, key, type):
        idx = self.hashMap.index(key)
        if type == 'v':
            return idx + 1
        else:
            return idx

    @staticmethod
    def __gethash__(invalue):
        key  = hashlib.md5(hashMap.__getutf8__(invalue)).hexdigest()[:2]
        return int(key,16)

    @staticmethod
    def __getutf8__(invalue):
        return invalue.encode('utf-8')
