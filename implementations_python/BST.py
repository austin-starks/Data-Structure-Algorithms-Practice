class BSTNode(object):
  """
  Implementation of a Node for a Binary Search Tree

  This Node stores a value and the left and right children trees. This node also
  stores the amount of nodes in the binary search tree has a particular value 
  (in order to handle duplicate insertions).

  Class invariant:
    - self.value: the value stored in the BST (an int)
    - self.left: the left child of the BST (a BSTNode)
    - self.right: the right child of the BST (a BSTNode)
    - self.count: the number of times this node is in the BST (an int)
    - self.parent: the parent of this Node (a BSTNode or None if the root)
  """
  def __init__(self, value, parent = None):
    """
    Initializes a BSTNode.

    Class invariant:
      - self.value: the value stored in the BST (an int)
      - self.left: the left child of the BST (a BSTNode)
      - self.right: the right child of the BST (a BSTNode)
      - self.count: the number of times this node is in the BST (an int)
      - self.parent: the parent of this Node (a BSTNode or None if the root)
    """
    self.value = value
    self.left = None 
    self.right = None
    self.count = 1
    self.parent = parent
  
  def get_value(self):
    """
    Returns: the value stored in the Binary Search tree
    """
    return self.value
  
  def insert(self, value):
    """
    Inserts the value into the Binary Search Tree

    This function recursively transverses the children to find the location to 
    insert the value.

    If the value already exists in the tree, the count parameter is incremented 
    by one. 

    Returns: the number of times the value was inserted into the tree
    """
    if value == self.value:
      self.count = self.count + 1 
      return self.count
    if value < self.value:
      if self.left == None:
        self.left = BSTNode(value, self)
        return 1
      else:
        return self.left.insert(value) 
    else:
      if self.right == None:
        self.right = BSTNode(value, self)
        return 1
      else:
        return self.right.insert(value) 
  
  def find_node(self, value : int):
    """
    Finds the given value in the Node or in its children

    This function attempts to find the value in this Node or in the children. 
    If it exist, this function returns the Node with that value. 

    Parameter value: the value to find 
    Precondition: value is an int

    Returns: a BSTNode or None
    """
    if self.value == value:
      return self 
    elif value < self.value: 
      return None if self.left is None else self.left.find_node(value)
    else:
      return None if self.right is None else self.right.find_node(value)

  def max_leaf(self):
    """
    Finds the maximum value'd child from this node.

    This node finds the node with the child containing the maximum value and 
    returns it.

    Returns: a node with the highest value
    """
    if self.right is not None:
      return self.right.max_leaf()
    else:
      return self

  def preorder(self, arr) -> list:
    """
    Gives the preorder traversal of this node

    This function returns a list representing the preorder traversal

    Returns: a list representing the preorder traversal
    """
    if self:
      arr.append(self.value)
      if self.left:
        self.left.preorder(arr)
      if self.right:
        self.right.preorder(arr)
    return arr

  def inorder(self, arr) -> list:
    """
    Gives the inorder traversal of this node

    This function returns a list representing the inorder traversal

    Returns: a list representing the inorder traversal
    """
    if self:
      if self.left:
        self.left.inorder(arr)
      arr.append(self.value)
      if self.right:
        self.right.inorder(arr)
    return arr

  def delete(self, value, force_delete, root) -> int:
    """
    Deletes the node with value from the Binary Search Tree

    This function calls the find method to get the node to delete. It then 
    removes the ndoe from the tree. If the node was inserted twice, it won't be 
    deleted.

    Parameter value: the value to insert 
    Precondition: value is an int 

    Parameter force_delete: whether or not to remove the node if the count is
                            not 0
    Precondition: force_delete is a bool

    Returns: the number of times the node was inserted into the tree before 
    deleting
    """
    pass

  def postorder(self, arr) -> list:
    """
    Gives the postorder traversal of this node

    This function returns a list representing the postorder traversal

    Returns: a list representing the postorder traversal
    """
    if self:
      if self.left:
        self.left.postorder(arr)
      if self.right:
        self.right.postorder(arr)
      arr.append(self.value)
    return arr
      


class BinarySearchTree(object):
  """
  Implementation of a Binary Search Tree

  This implementation uses BSTNode to keep track of the left and right children 
  of the Binary Search Tree. This class also implements insert, delete, and find.

  Class invariant:
    - self.root_value: the root of this binary search tree (a BSTNode)
  """
  
  def __init__(self, root_value : int = None):
    """
    Initializes a Binary Search Tree

    Class invariant:
      - self.root: the root of this binary search tree (a BSTNode)

    Parameter root_value: the value for the root of the tree
    Precondition: root_value is an int
    """
    if root_value is None:
      self.root = None
    else: 
      self.root = BSTNode(root_value, None) 

  def insert(self, value : int) -> int:
    """
    Inserts a node value into the Binary Search Tree

    If the root exists, this function calls the recursive insert function for 
    the root node. Otherwise, this function creates a new root. 

    Returns: the number of times the node has been inserted into the tree.
    """
    if self.root == None:
      self.root = BSTNode(value)
      return self.root.count
    else:
      return self.root.insert(value)
    
  def find(self, value : int) -> int:
    """
    Finds the given value in the Node or in its children

    This function calls the recursive find function for the root node.

    Parameter value: the value to find 
    Precondition: value is an int

    Returns: the number of times the value has been inserted into the tree 
    (of if it hasn't been inserted)
    """
    found_node = self.root.find_node(value)
    return 0 if found_node == None else found_node.count

  def preorder(self) -> list:
    """
    Returns the preorder traversal of the tree

    This function calls the recursive preorder function for the root node, and 
    returns a list with that traversal pattern.
    """
    return self.root.preorder([]) 

  def inorder(self) -> list:
    """
    Returns the inorder traversal of the tree

    This function calls the recursive inorder function for the root node, and 
    returns a list with that traversal pattern.
    """
    return self.root.inorder([]) 

  def postorder(self) -> list:
    """
    Returns the postorder traversal of the tree

    This function calls the recursive postorder function for the root node, and 
    returns a list with that traversal pattern.
    """
    return self.root.postorder([]) 

  def delete(self, value : int, force_delete : bool = False) -> int:
    """
    Deletes the node with value from the Binary Search Tree

    This function calls the delete function for the root node.

    Parameter value: the value to insert 
    Precondition: value is an int 

    Parameter force_delete: whether or not to remove the node if the count is
                            not 0
    Precondition: force_delete is a bool

    Returns: the number of times the value was inserted into the tree before 
    deleting it (0 if the value was not in the tree)
    """
    count = self.root.delete(value, force_delete, self.root)
    return count

    