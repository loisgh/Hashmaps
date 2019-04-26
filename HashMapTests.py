import unittest
import mock
from HashMap import HashMap


class HashMapTests(unittest.TestCase):

    def testhash(self):
        thehash = HashMap._gethash("hello")
        self.assertEqual(thehash.__class__.__name__, 'int')
        self.assertEqual(HashMap._gethash("hello"), hash("hello") % 255)

    def testhashadd(self):
        myhash = HashMap()
        myhash.add("something", 99)
        self.assertEqual(myhash.HashMap[HashMap._gethash("something")], ["something", 99])
        # add same key different value
        myhash.add("something", 100)
        self.assertEqual(myhash.HashMap[HashMap._gethash("something")], ["something", 100])
        self.assertEqual(myhash.length, 1)
        # add another value make sure length has been incremented
        myhash.add("something else", 105)
        self.assertEqual(myhash.HashMap[HashMap._gethash("something else")], ["something else", 105])
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
        self.assertEqual(myhash.size(), 1)
        myhash.add("something more", 198)
        self.assertEqual(myhash.size(), 2)
        myhash.add("something more", 198)
        self.assertEqual(myhash.size(), 2)
        myhash.add("something even more", 198)
        self.assertEqual(myhash.size(), 3)
        myhash.remove("something even more")
        self.assertEqual(myhash.size(), 2)


    @mock.patch('HashMap.HashMap._gethash')
    def testhashclash(self, mock_gethash):
        mock_gethash.return_value = 25
        myhash = HashMap()
        myhash.add("something", 99)
        result = myhash.HashMap[25]
        self.assertEqual(result, ['something', 99])
        myhash.add("duplicate", 100)
        result = myhash.HashMap[25]
        self.assertEqual(result, ['something', 99, 'duplicate', 100])
        myhash.add("one last thing", 101)
        result = myhash.HashMap[25]
        self.assertEqual(result, ['something', 99, 'duplicate', 100, 'one last thing', 101])
        self.assertEqual(myhash.get('something'), 99)
        self.assertEqual(myhash.get('duplicate'), 100)
        self.assertEqual(myhash.get('one last thing'), 101)
        self.assertEqual(myhash.size(), 3)
        myhash.remove('duplicate')
        result = myhash.HashMap[25]
        self.assertEqual(result, ['something', 99, 'one last thing', 101])
        self.assertEqual(myhash.size(), 2)
        myhash.remove('one last thing')
        result = myhash.HashMap[25]
        self.assertEqual(result, ['something', 99])
        self.assertEqual(myhash.size(), 1)
        myhash.remove('something')
        result = myhash.HashMap[25]
        self.assertEqual(result, None)
        self.assertEqual(myhash.size(), 0)