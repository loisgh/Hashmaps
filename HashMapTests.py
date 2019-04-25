import unittest
from unittest.mock import patch
import mock
from HashMap import *

# Return hashclash data from methods using @patch
# See that hashclash methods return correct data
# TODO First Verify that hashclash functions work by changing hash method

class HashMapTests(unittest.TestCase):

    def testhash(self):
        thehash = HashMap.__gethash__("hello")
        self.assertEqual(thehash.__class__.__name__, 'int')
        self.assertEqual(HashMap.__gethash__("hello"), hash("hello") % 255)

    def testhashadd(self):
        myhash = HashMap()
        myhash.add("something", 99)
        self.assertEqual(myhash.HashMap[HashMap.__gethash__("something")], ["something", 99])
        # add same key different value
        myhash.add("something", 100)
        self.assertEqual(myhash.HashMap[HashMap.__gethash__("something")], ["something", 100])
        self.assertEqual(myhash.length, 1)
        # add another value make sure length has been incremented
        myhash.add("something else", 105)
        self.assertEqual(myhash.HashMap[HashMap.__gethash__("something else")], ["something else", 105])
        self.assertEqual(myhash.size(), 2)

    def testhashget(self):
        myhash = HashMap()
        myhash.add("something", 99)
        self.assertEqual(myhash.get("something"), 99)
        self.assertEqual(myhash.get("nothing"), None)

        # with mock.patch('HashMap.__gethash__', ) as mock_gethash:
        #     mock_gethash.return_value = 25
        # myhash.add("hashclash1", 75)
        # myhash.add("hashclash2", 175)
        # self.assertEqual(myhash.get("hashclash1"), 75)
        # self.assertEqual(myhash.get("hashclash2"), 175)

    def testhashremove(self):
        myhash = HashMap()
        myhash.add("something", 99)
        myhash.add("something else", 199)
        self.assertEqual(myhash.size(), 2)
        myhash.remove("something")
        self.assertEqual(myhash.size(), 1)
        myhash.remove("not there")
        self.assertEqual(myhash.size(), 1)

    def testgetsize(self):
        myhash = HashMap()
        myhash.add("something", 99)
        self.assertEqual(myhash.size(), 1)
        myhash.add("something more", 198)
        self.assertEqual(myhash.size(), 2)
        myhash.add("something more", 198)
        self.assertEqual(myhash.size(), 2)
        myhash.add("something even more", 198)
        self.assertEqual(myhash.size(), 3)
        myhash.remove("something even more")
        self.assertEqual(myhash.size(), 2)