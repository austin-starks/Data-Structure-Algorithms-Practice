class TreeNode(object):
  """
  Implementation of a TreeNode 

  A TreeNode is a Node with a value and a list of children. Each child is also 
  a TreeNode

  Class invariants:
    - self.value:     The value for this TreeNode : Any
    - self.children:  The list of children for this Node : TreeNode List
  """
  def __init__(self, value, parent = None):
    """
    Initializes a TreeNode 

    Parameter value: the value for this TreeNode

    Class invariants:
      - self.value:     The value for this TreeNode : Any
      - self.children:  The list of children for this Node : TreeNode List
    """
    self.value = value 
    self.children = []
    self.parent = parent
  
  def add_child(self, value):
    """
    Adds a value to the list of children for this node

    Parameter value: the value to add to the Tree 
    Precondition: value is not a TreeNode
    """
    assert type(value) != TreeNode
    self.children.append(TreeNode(value, self)) 

  def height(self):
    """
    The height of the Tree 

    This function recursively computes the height of the tree from the root.
    It computes the height of each child and returns the maximum height

    Returns: the height of the tree (int) 
    """
    if self.children == []:
      return 1 
    else:
      arr = []
      for child in self.children:
        result = 1 + child.height()
        arr.append(result)
      return max(arr)
  
  def get_children(self):
    """
    Returns: the children for this tree (TreeNode List)
    """
    return self.children
  
  def get_value(self):
    """
    Returns: the value for this TreeNode
    """
    return self.value