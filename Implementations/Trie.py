class TrieNode(object):
  """
  Implementation of a trie 
  Picture of a trie:
        root
    /   \      \ 
    t   a       b
    |   |       |
    h   n       y
    |   |   \   |
    e   s   y   e
  /  |   |  |   |
  i  r   w *** ***
  |  |   |
  r  e   e
  | |    |
*** ***  r
         |
        ***

  Class invariant:
    - self.data: the data that this TrieNode stores (or the empty string if no data)
    - self.char: the character this TrieNode encodes for (or * if the root)
    - self.children: the children characters for this node (and *** if the path 
                      to this node is a complete word.)
    - self.parent: the parent to this Node (or None if this is the root node)

  Resources on tries: 
    - https://en.wikipedia.org/wiki/Trie
    - https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
    - https://www.youtube.com/watch?v=zIjfhVPRZCg
    - https://www.youtube.com/watch?v=o6563NNbdtg 
  """
  def __init__(self, data = ""):
    """
    Initializes a TrieNode 
    
    Parameter data: the data this node stores 
    
    Class invariant:
    - self.data: the data that this TrieNode stores (or the empty string if no data)
    - self.char: the character this TrieNode encodes for (or * if the root)
    - self.children: the children characters for this node (and *** if the path 
                      to this node is a complete word.)
    - self.parent: the parent to this Node (or None if this is the root node)
    """
    self.char = "*" 
    self.data = data
    self.children : Dict[str, Node] = {}
    self.parent : TrieNode = None

  def insert(self, key : str, data = "") -> None :
    """
    Inserts the key into the trie. Optionallly, can insert a value into the trie.

    Parameter data: the data to store
    Paraneter key: the word to store in the trie 

    Precondition: key is a string 
    """
    for char in key:
      if char not in self.children:
        self.children[char] = TrieNode(data)
      parent = self
      self = self.children[char]
      self.char = char 
      self.parent = parent
    self.children["*"] = char
  
  def find_value(self, key : str):
    """
    Returns one of the following:  
    - The data stored in the key if any data is stored in the tree 
    - The empty string if the key is in the dictionary but has no data 
    - None if the key isn't in the trie.

    Precondition: key is a string
    """
    for char in key:
      if char in self.children:
        self = self.children[char] 
      else:
        return None 
    if "*" in self.children:
      return self.data
    else:
      return None
    
  def contains_prefix(self, key : str) -> bool:
    """
    Returns: True if the prefix is in the trie; False otherwise

    Precondition: key is a string
    """
    for char in key:
      if char in self.children:
        self = self.children[char]
      else:
        return False 
    return True

