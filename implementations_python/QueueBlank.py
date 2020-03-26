class QueueArray(object):
  """
  Implementation of Queue using an array.

  A QueueArray is an array representation of a queue. Values are added to the 
  array from back to front. 

  Example: 
    - q = QueueArray(5)
    - print(q) ==> [5]
    - q.enqueue(3)
    - q.enqueue(6)
    - q.enqueue(9)
    - print(q) ==> [9,6,3,5]
    - q.queue()
    - print(q) ==> [9,6,3,5]

  Class invariants:
    - self._data: The data stored in the queue. The queue will be represented 
                  as an array that is not resizable. As more values are inserted 
                  into the array, the enqueue function increases the size of the 
                  array. 
    - self._max_size: The current max size of the queue. 
    - self._size:     The current size of the queue. 
  """
  def __init__(self, value=None):
    """
    Initializes a QueueArray 

    Parameter value: the value to insert into the Queue 

    Class invariants:
    - self._data: The data stored in the queue. The queue will be represented 
                  as an array that is not resizable. As more values are inserted 
                  into the array, the enqueue function increases the size of the 
                  array. 
    - self._max_size: The current max size of the queue. 
    - self._size:     The current size of the queue.
    """
    pass

  def enqueue(self, value):
    """
    Adds a value to this QueueArray

    This function adds a value to the queue array. If the current size is 
    greater than or equal to the maximum size, the array is re-sized to fit 
    more values into the array

    Parameter value: the value to insert 
    Precondition: value is not None
    """
    pass

  def queue(self):
    """
    Removes a value from the queue 

    This function removes the first item to be added to the QueueArray. This is 
    equivalent to removing the last item from the array data structure. 
    If the queue pops an empty value, the QueueArray is resized.

    Returns: the value that is removed or None if the QueueArray is empty
    """
    pass

  def peek(self):
    """
    Looks at the first item to be added to the queue. 

    This function returns the first item to be added to the queue, or the last 
    item of the array data structure.

    Returns: the first value to be added to the QueueArray
    """
    pass

  def isEmpty(self):
    """
    Returns whether the queue is empty. This is equivalent to returning if the 
    last value of the array data structure is None.

    Returns: True if the queue is empty; False otherwise
    """
    pass


    
