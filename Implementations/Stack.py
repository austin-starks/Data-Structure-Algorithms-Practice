import LinkedList

class LinkedListStack(LinkedList.LinkedList):
  """
  Implementation using LinkedList as a parent class. 
  """

  def __init__(self, value=None):
    super().__init__(value)
  
  def peek(self):
    """
    Returns: the data in the top of the stack
    """
    return self._head.getData()
  
  def push(self, data):
    """
    Adds a new element to the top of the stack
    """
    self.insert(data)

  def pop(self):
    """
    Removes the top element of the stack 
    """
    data = self.peek()   
    super().delete(self.peek())
    return data

  def isEmpty(self):
    return self._head is None

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
    self._data = [value, None, None, None, None]
    self._maxSize = 5 
    self._head = value 
    self._size = 0 if value is None else 1
  
   
  def peek(self):
    """
    Returns: the data in the top of the stack
    """
    return self._head

  def push(self, value):
    """
    Adds a new element to the top of the stack
    """
    if self._size == self._maxSize - 1:
      self._data = self._data + [None]*self._maxSize
      self._maxSize = self._maxSize * 2 
    self._data[self._size] = value 
    self._size += 1
    self._head = value
    
  def size(self):
    """
    Returns: the size of the linked list
    """
    return self._size

  def pop(self):
    """
    Removes the top element of the stack and returns the element removed
    """
    if self._size == 0:
      return None
    self._size -= 1
    val = self._data[self._size]
    self._data[self._size] = None
    if self._size > 0:
      self._head = self._data[self._size - 1]
    else:
      self._head = None
    return val

  def isEmpty(self):
    return self._head is None
    