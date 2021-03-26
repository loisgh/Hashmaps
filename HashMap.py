class HashMap:
    """This class is an implementation of a HashMap that uses lists and hashing under the hood """

    def __init__(self, capacity):
        """ The size is the number of idx locations that do not contain None """
        self.length = 0
        self.capacity = capacity
        self.HashMap = [None] * self.capacity

    def add(self, key, value):
        """
        This method allows you to add to the hashmap.
        :param key: Any string
        :param value: Any number or string
        :return: No return value.
        """
        threshhold = self.capacity * 0.75
        if self.length >= threshhold:
            self._increase_size()

        hashkey = self._gethash(key)
        if not self.HashMap[hashkey]:
            # The key does not exist so add it
            value_to_store = [key, value]
            self.HashMap[hashkey] = value_to_store
            self.length += 1
        elif self.HashMap[hashkey] and key not in self.HashMap[hashkey]:
            # There is a hashclash append to the location
            self.HashMap[hashkey].extend([key, value])
            self.length += 1
        else:
            # The key exists and matches so the value gets overlayed
            self.HashMap[hashkey] = [key, value]

    def get(self, key):
        """
        Returns the value for a given key
        :param key:
        :return: the value stored in the hashmap
        """
        hashkey = self._gethash(key)
        if type(self.HashMap[hashkey]) is list:
            if len(self.HashMap[hashkey]) > 2:
                # Return correct Key and value from the location which has a hashclash
                idx = self._find_if_hashclash(key, hashkey, "v")
                if idx is not None:
                    return self.HashMap[hashkey][idx]
            elif self.HashMap[hashkey][0] == key:
                # Check that the data matches the key and return it if it does
                return self.HashMap[hashkey][1]

    def remove(self, key):
        """
        Removes the value for the given key. Subtracts from length.
        :param key:
        :return: No return value.
        """
        thekey = self._gethash(key)
        if self.HashMap[thekey] is not None:
            if len(self.HashMap[thekey]) == 2:
                self.HashMap[
                    self._gethash(key)
                ] = None  # Keep the location but set the value to None
            else:
                hashkey = self._gethash(key)
                idx = self._find_if_hashclash(key, hashkey, "i")
                self.HashMap[hashkey].pop(idx)
                self.HashMap[hashkey].pop(idx)
            self.length -= 1

    def size(self):
        return self.length

    def _find_if_hashclash(self, key, location, key_or_value):
        """
        Find the key or value when there is a hashclash.
        In the event of a hashclash there will be more than one key, value pair for a list item.
        This method finds the correct one and returns the idx of the key or value.  If no key is
        found than None is returned.
        :param key:
        :param location:
        :param key_or_value:
        :return: idx or the key or value within the list item.
        """
        idx = (
            self.HashMap[location].index(key) if key in self.HashMap[location] else None
        )
        if idx is not None:
            if key_or_value == "v":
                return idx + 1
            else:
                return idx

    def _gethash(self, invalue):
        """ return a hash using the pythons hash method """
        return hash(invalue) % self.capacity

    def _increase_size(self):
        keys_vals_to_move = [item for item in self.HashMap if item]
        self.length = 0
        self.capacity = self.capacity * 2
        self.HashMap = [None] * self.capacity
        for item in keys_vals_to_move:
            while len(item) > 0:
                self.add(item[0], item[1])
                item.pop(0)
                item.pop(0)

    def __str__(self):
        return "scapacity of hash: {}, current size of hash: {}".format(
            self.capacity, self.length
        )

    def __repr__(self):
        return "capacity of hash: {}, current size of hash: {}".format(
            self.capacity, self.length
        )

    def __getitem__(self, arg):
        return self.get(arg)

    def __setitem__(self, key, val):
        return self.add(key, val)