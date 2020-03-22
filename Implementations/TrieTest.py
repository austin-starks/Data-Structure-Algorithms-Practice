from Trie import *
# change from Trie to from TreeBlank


def tests():
  print("Test Tries")
  trie = TrieNode()
  print("Test insert and find")
  trie.insert("skittles", 1.99)
  trie.insert("m&m's", 1.49)
  trie.insert("xbox 360", 299.99)
  trie.insert("ps4", 299.99)
  trie.insert("gameboy")
  assert trie.find_value("xbox") == None
  assert trie.find_value("xbox 360") == 299.99
  assert trie.find_value("m&m's") == 1.49
  assert trie.find_value("m&ms") == None
  assert trie.find_value("gameboy") == ""
  print("Insert and find tests complete")
  print("Test contains prefix")
  assert trie.contains_prefix("m&m")
  assert trie.contains_prefix("xbox")
  assert not trie.contains_prefix("skittless")
  assert not trie.contains_prefix("skitttles")
  print("Contains substring test complete")
  print("Tries tests complete")


