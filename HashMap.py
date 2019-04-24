import hashlib


class HashMap:

    def __init__(self):
        self.length = 0
        self.HashMap = [None] * 255

    def add(self, key, value):
        hashkey = HashMap.__gethash__(key)
        if not self.HashMap[hashkey]:
            value_to_store = [key, value]
            self.HashMap.insert(hashkey, value_to_store)
            self.length += 1
        elif self.HashMap[hashkey][0] != key:
            self.HashMap[hashkey].append(key)
            self.HashMap[hashkey].append(value)
            self.length += 1
        else:
            self.HashMap[hashkey][1] = value

    def get(self, key):
        hashkey = HashMap.__gethash__(key)
        if self.HashMap[hashkey]:
            if len(self.HashMap[hashkey]) > 2:
                idx = self.__find_if_hashclash__(hashkey, 'v')
                return self.HashMap[hashkey][idx]
            else:
                return self.HashMap[hashkey][1]
        else:
            return None

    def remove(self, key):
        thekey = HashMap.__gethash__(key)
        if self.HashMap[thekey]:
            if len(self.HashMap[thekey]) == 2:
                self.HashMap[HashMap.__gethash__(key)] = None
            else:
                hashkey = HashMap.__gethash__(key)
                idx = self.__find_if_hashclash__(hashkey, 'i')
                self.HashMap[hashkey].pop(idx)
                self.HashMap[hashkey].pop(idx+1)
            self.length -= 1

    def size(self):
        return self.length

    def contains_key(self, key):
        hashkey = HashMap.__gethash__(key)
        if self.HashMap[hashkey]:
            if len(self.HashMap[hashkey]) > 2:
                idx = self.__find_if_hashclash__(hashkey, 'v')
                if self.HashMap[hashkey][idx]:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def __find_if_hashclash__(self, key, key_or_value):
        idx = self.HashMap.index(key)
        if key_or_value == 'v':
            return idx + 1
        else:
            return idx

    @staticmethod
    def __gethash__(invalue):
        key = hashlib.md5(HashMap.__getutf8__(invalue)).hexdigest()[:2]
        return int(key, 16)

    @staticmethod
    def __getutf8__(invalue):
        return invalue.encode('utf-8')
