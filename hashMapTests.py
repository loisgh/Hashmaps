import unittest
import mock
from HashMap import *

# TODO Review how to patch
# Return hashclash data from methods using @patch
# See that hashclash methods return correct data


class HashMapTests(unittest.TestCase):

    def testutf8(self):
        the_bytes = HashMap.__getutf8__("hello")
        self.assertEqual(the_bytes.__class__.__name__, 'bytes')

        the_bytes = HashMap.__getutf8__("hello")
        self.assertNotEqual(the_bytes.__class__.__name__, 'int')

    def testhash(self):
        thehash = HashMap.__gethash__("hello")
        self.assertEqual(thehash.__class__.__name__, 'int')

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
        myhash.add("something more", 198)
        self.assertEqual(myhash.size(), 2)

    def testhashcontainskey(self):
        myhash = HashMap()
        myhash.add("something", 99)
        self.assertEqual(myhash.containsKey("something"), True)
        self.assertEqual(myhash.containsKey("nothing"), False)
