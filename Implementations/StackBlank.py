import LinkedList

class LinkedListStack(LinkedList.LinkedList):
  """
  Implementation of a Stack using LinkedList

  This class uses LinkedList as a parent class. The push function adds the 
  data to the linked list. The pop function deletes the first item of the  
  linked list

  Class invariant:
    - value: the value in the stack
  """

  def __init__(self, value=None):
    """
    Initializes a LinkedListStack 

    Parameter value: the value to initialize the StackArray with

    Class invariant:
    - value: the value in the stack
    """
    pass
  
  def peek(self):
    """
    Looks at the top of the stack 

    Returns: the data in the top of the stack
    """
    pass
  
  def push(self, data):
    """
    Adds a new element to the top of the stack 

    This function adds a value to the to the stack. It calls the insert function 
    in the parent class, which does all of the work.

    Parameter value: the value to add to the stack
    Precondition: value is not None
    """
    pass

  def pop(self):
    """
    Removes a value from the stack 

    This function removes the last item to be added to the StackArray. It does 
    this by calling the delete function on the last item to be added to the Stack

    Returns: the value that is removed or None if the StackArray is empty
    """
    pass

  def isEmpty(self):
     """
    Returns whether the stack is empty. This is equivalent to returning if the 
    head of the stack is equal to None

    Returns: True if the Stack is empty; False otherwise
    """
    pass

  def delete(self, *args):
    """
    Raises: Attribute Error. Stacks don't typically have a delete function
    """
    raise AttributeError("LinkedListStack has no function delete")


class StackArray(object):
  """
  Implementation of Stack using an array.

  A StackArray is an array representation of a Stack. Values are added to the 
  array from back to front. 

  Example: 
    - s = StackArray(5)
    - print(s) ==> [5]
    - s.push(3)
    - s.push(6)
    - s.push(9)
    - print(s) ==> [5,3,6,9]
    - s.pop()
    - print(s) ==> [5,3,6]

  Class invariants:
    - self._data: The data stored in the Stack. The Stack will be represented 
                  as an array that is not resizable. As more values are inserted 
                  into the array, the pop function increases the size of the 
                  array. 
    - self._max_size: The current max size of the Stack. 
    - self._size:     The current size of the Stack. 
    - self._head:     The head of the Stack (the last item to be added to the stack)
  """

  def __init__(self, value = None):
    """
    Initializes a StackArray 

    Parameter value: the value to insert into the Stack 

    Class invariants:
    - self._data: The data stored in the stack. The stack will be represented 
                  as a fixed sized array. As more values are inserted into the 
                  array, the push function increases the size of the array. 
    - self._max_size: The current max size of the Stack. 
    - self._size:     The current size of the Stack.
    - self._head:     The head of the Stack (the last item to be added to the stack)
    """
    pass
  
   
  def peek(self):
    """
    Looks at the top of the stack 

    Returns: the data in the top of the stack
    """
    pass

  def push(self, value) -> None:
    """
    Adds a new element to the top of the stack 

    This function adds a value to the to the stack. If the size of the stack 
    is near the size of the internal array, the array increases in size.

    Parameter value: the value to add to the stack
    Precondition: value is not None
    """
    pass
    
  def size(self) -> int:
    """
    Returns: the size of the stack
    """
    pass

  def pop(self):
    """
    Removes a value from the stack 

    This function removes the last item to be added to the StackArray. It does 
    this by changing the last value of the array to None, and then reassigning 
    the head variable to be the next item to be added to the stack.

    Returns: the value that is removed or None if the StackArray is empty
    """
    pass

  def isEmpty(self):
    """
    Returns whether the stack is empty. This is equivalent to returning if the 
    head of the stack is equal to None

    Returns: True if the Stack is empty; False otherwise
    """
    pass
    