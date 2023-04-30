from __future__ import annotations

from typing import Any, List, Optional


class HashMap:
    """
    This class is an implementation of a HashMap that uses lists and
    hashing under the hood
    """

    length: int
    capacity: int
    HashMap: List[Any]

    def __init__(self, capacity: int):
        """
        :param capacity: The max possible size of the HashMap
        """
        self.length = 0
        self.capacity = capacity
        self.HashMap = [None] * self.capacity

    def add(self, key: str, value: str) -> Optional[None]:
        """
        This method allows you to add to the hashmap.

        :param key: Any string
        :param value: Any number or string
        :returns: no value
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

    def get(self, key: str) -> str:
        """
        Returns the value for a given key

        :param key: A string with the value of the key
        :returns: the corresponding value stored in the hashmap
        """
        hashkey = self._gethash(key)
        if type(self.HashMap[hashkey]) is list:
            if len(self.HashMap[hashkey]) > 2:
                """
                Return correct Key and value from the
                location which has a hashclash
                """
                idx = self._find_if_hashclash(key, hashkey, "v")
                if idx is not None:
                    return self.HashMap[hashkey][idx]
            elif self.HashMap[hashkey][0] == key:
                # Check that the data matches the key and return it if it does
                return self.HashMap[hashkey][1]
        return ""

    def remove(self, key: str) -> None:
        """
        Removes the value for the given key. Subtracts from length.

        :param key: string
        :returns: no value.
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

    def size(self) -> int:
        """
        This method returns the length of the HashMap.
        This is the number of non None values.

        :returns: int that represents the number of
                    non null values
        """
        return self.length

    def _find_if_hashclash(self, key: str, location: int, key_or_value: str):
        """
        Find the key or value when there is a hashclash.
        In the event of a hashclash there will be more than one key,
        value pair for a list item.
        This method finds the correct one and returns the idx of
        the key or value.
        If no key is found than None is returned.
        :param key:
        :param location:
        :param key_or_value:
        :return: idx or the key or value within the list item.
        """
        if key in self.HashMap[location]:
            idx = self.HashMap[location].index(key)
        else:
            idx = None

        if idx is not None:
            if key_or_value == "v":
                return idx + 1
            else:
                return idx

    def _gethash(self, invalue) -> int:
        """
        return a hash using the pythons hash method
        :param invalue: value to hash
        """
        return hash(invalue) % self.capacity

    def _increase_size(self) -> None:
        """
        Take the current hash and increase the capacity.
        This involves rehashing and moving the values to new locations
        based on the new size of the Hash.
        :return: no value
        """
        keys_vals_to_move = [item for item in self.HashMap if item]
        self.length = 0
        self.capacity = self.capacity * 2
        self.HashMap = [None] * self.capacity
        for item in keys_vals_to_move:
            while len(item) > 0:
                self.add(item[0], item[1])
                item.pop(0)
                item.pop(0)

    def __str__(self) -> str:
        """
        String representation of HashMap
        :return: String with capacity and current size
        """
        return "scapacity of hash: {}, current size of hash: {}".format(
            self.capacity, self.length
        )

    def __repr__(self) -> str:
        """
        String representation of HashMap
        :return: String with capacity and current size
        """
        return "capacity of hash: {}, current size of hash: {}".format(
            self.capacity, self.length
        )

    def __getitem__(self, key: str) -> str:
        """
        Wrapper function to allow use of bracket notation
        in retrieving the value of the key.

        :param key: Key of the Hashed Item
        :return: Value of Key
        """
        return self.get(key)

    def __setitem__(self, key: str, val: str) -> None:
        """
        Wrapper function to allow use of bracket notation
        in setting the value of the key.

        :param key: Key of the Hashed item
        :param value: Value of the Hashed item
        """
        return self.add(key, val)
