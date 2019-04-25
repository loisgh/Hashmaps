class HashMap:

    def __init__(self):
        self.length = 0
        self.HashMap = [None] * 255

    def add(self, key, value):
        hashkey = HashMap.__gethash__(key)
        if type(self.HashMap[hashkey]) is list:
            if self.HashMap[hashkey][0] != key:  # There is a hashclash append to the location
                self.HashMap[hashkey].append(key)
                self.HashMap[hashkey].append(value)
                self.length += 1
            else:                               # The key exists and matches so overlay the value
                self.HashMap[hashkey] = [key, value]
        else:                                   # The key does not exist so add it
            value_to_store = [key, value]
            self.HashMap[hashkey] = value_to_store
            self.length += 1

    def get(self, key):
        hashkey = HashMap.__gethash__(key)
        if type(self.HashMap[hashkey]) is list:
            if len(self.HashMap[hashkey]) > 2:
                idx = self.__find_if_hashclash__(key, hashkey, 'v')
                if idx is not None:
                    return self.HashMap[hashkey][idx]
                else:
                    return None
            elif self.HashMap[hashkey][0] == key:
                return self.HashMap[hashkey][1]
            else:
                return None
        else:
            return None

    def remove(self, key):
        thekey = HashMap.__gethash__(key)
        if self.HashMap[thekey] is not None:
            if len(self.HashMap[thekey]) == 2:
                self.HashMap[HashMap.__gethash__(key)] = None   # Keep the location but set the value to None
            else:
                hashkey = HashMap.__gethash__(key)
                idx = self.__find_if_hashclash__(key, hashkey, 'i')
                self.HashMap[hashkey].pop(idx)
                self.HashMap[hashkey].pop(idx)
            self.length -= 1

    def size(self):
        return self.length

    def __find_if_hashclash__(self, key, location, key_or_value):
        idx = self.HashMap[location].index(key) if key in self.HashMap[location] else None
        if idx is not None:
            if key_or_value == 'v':
                return idx + 1
            else:
                return idx

    @staticmethod
    def __gethash__(invalue):
        return hash(invalue) % 255