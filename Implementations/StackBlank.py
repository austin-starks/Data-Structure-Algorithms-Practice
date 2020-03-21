import LinkedList

class LinkedListStack(LinkedList.LinkedList):
  """
  Implementation using LinkedList as a parent class. 
  """

  def __init__(self, value=None):
    pass
  
  def peek(self):
    """
    Returns: the data in the top of the stack
    """
    pass
  
  def push(self, data):
    """
    Adds a new element to the top of the stack
    """
    pass

  def pop(self):
    """
    Removes the top element of the stack 
    """
    pass

  def isEmpty(self):
    pass

  def delete(self, *args):
    """
    Raises: Attribute Error. LinkedLists can't implement delete
    """
    raise AttributeError("LinkedList Stack has no function delete")


class LinkedListArray(object):
  """
  Implementation of LinkedList using a fixed size array. Python doesn't have 
  a fixed size array, so I used array. You could instead use a regular array 
  and use methods like append and pop (but I wanted to make it realistic).

  There is more than one correct implementation; as long as your complexity is 
  good, you're good.
  """

  def __init__(self, value = None):
    pass
  
   
  def peek(self):
    """
    Returns: the data in the top of the stack
    """
    pass

  def push(self, value):
    """
    Adds a new element to the top of the stack
    """
    pass
    
  def size(self):
    """
    Returns: the size of the linked list
    """
    pass

  def pop(self):
    """
    Removes the top element of the stack and returns the element removed
    """
    pass

  def isEmpty(self):
    pass
    