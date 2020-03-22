class TreeNode(object):
  """
  Implementation of a TreeNode 

  A TreeNode is a Node with a value and a list of children. Each child is also 
  a TreeNode

  Class invariants:
    - self.value:     The value for this TreeNode : Any
    - self.children:  The list of children for this Node : TreeNode List
  """
  def __init__(self, value, children = [], parent = None):
    """
    Initializes a TreeNode 

    Parameter value: the value for this TreeNode

    Class invariants:
      - self.value:     The value for this TreeNode : Any
      - self.children:  The list of children for this Node : TreeNode List
    """
    pass
  
  def add_child(self, value, children = []) -> None:
    """
    Returns whether the stack is empty. This is equivalent to returning if the 
    head of the stack is equal to None

    Returns: True if the Stack is empty; False otherwise
    """
    pass 

  def height(self):
    """
    The height of the Tree 

    This function recursively computes the height of the tree from the root.
    It computes the height of each child and returns the maximum height

    Returns: the height of the tree (int) 
    """
    pass
  
  def get_children(self):
    """
    Returns: the children for this tree (TreeNode List)
    """
    pass
  
  def get_value(self):
    """
    Returns: the value for this TreeNode
    """
    pass