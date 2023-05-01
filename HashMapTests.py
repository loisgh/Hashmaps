import mock
from HashMap import HashMap


def testhash():
    capacity = 255
    myhash = HashMap(capacity)
    thehash = myhash._gethash("hello")
    assert thehash.__class__.__name__ == "int"
    assert myhash._gethash("hello") == hash("hello") % capacity

def testhashadd():
    myhash = HashMap(255)
    myhash.add("something", 99)
    assert myhash.HashMap[myhash._gethash("something")] == ["something", 99]
    assert myhash["something"] == 99
    # add same key different value
    myhash.add("something", 100)
    assert myhash.HashMap[myhash._gethash("something")] == ["something", 100]
    assert myhash.length == 1
    # add another value make sure length has been incremented
    myhash.add("something else", 105)
    assert myhash.HashMap[myhash._gethash("something else")] == ["something else", 105]
    assert myhash.size() == 2
    myhash["another thing"] = 299
    assert myhash.size() == 3
    assert myhash["another thing"] == 299

def testhashget():
    myhash = HashMap(255)
    myhash.add("something", 99)
    assert myhash.get("something") == 99
    assert myhash.get("nothing") == ''

def testhashremove():
    myhash = HashMap(255)
    myhash.add("something", 99)
    myhash.add("something else", 199)
    assert myhash.size() == 2
    myhash.remove("something")
    assert myhash.size() == 1
    myhash.remove("not there")
    assert myhash.size() == 1

def testgetsize():
    myhash = HashMap(255)
    myhash.add("something", 99)
    assert myhash.size() == 1
    myhash.add("something more", 198)
    assert myhash.size() == 2
    myhash.add("something more", 198)
    assert myhash.size() == 2
    myhash.add("something even more", 198)
    assert myhash.size() == 3
    myhash.remove("something even more")
    assert myhash.size() == 2

@mock.patch("HashMap.HashMap._gethash")
def testhashclash(mock_gethash):
    mock_gethash.return_value = 25
    myhash = HashMap(255)
    myhash.add("something", 99)
    result = myhash.HashMap[25]
    assert result == ["something", 99]
    myhash.add("duplicate", 100)
    result = myhash.HashMap[25]
    assert result == ["something", 99, "duplicate", 100]
    myhash.add("one last thing", 101)
    result = myhash.HashMap[25]
    assert result == ["something", 99, "duplicate", 100, "one last thing", 101]
    assert myhash.get("something") == 99
    assert myhash.get("duplicate") == 100
    assert myhash.get("one last thing") == 101
    assert myhash.size() == 3
    myhash.remove("duplicate")
    result = myhash.HashMap[25]
    assert result == ["something", 99, "one last thing", 101]
    assert myhash.size() == 2
    myhash.remove("one last thing")
    result = myhash.HashMap[25]
    assert result == ["something", 99]
    assert myhash.size() == 1
    myhash.remove("something")
    result = myhash.HashMap[25]
    assert result == None
    assert myhash.size() == 0

def testincreasesize():
    myhash = HashMap(4)
    assert myhash.capacity == 4
    myhash.add("one", 11)
    myhash.add("two", 22)
    myhash.add("three", 33)
    myhash.add("four", 44)
    assert myhash.capacity == 8
    assert myhash.get("one") == 11
    assert myhash.get("two") == 22
    assert myhash.get("three") == 33
    assert myhash.get("four") == 44
