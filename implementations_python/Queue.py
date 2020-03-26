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
    self._data = [None] * 4 + [value]
    self._max_size = 5 
    self._size = 0 if value is None else 1

  def __str__(self):
    """
    Prints the string representation of queue
    """
    string = ""
    for i in range(self._max_size):
      if not self._data[i] is None:
        string = string + " [" + str(self._data[i]) + "] "
        if i < self._max_size - 1:
          string = string + "->" 
    return string
  
  def __repr__(self):
    """
    Prints the string representation of queue
    """
    string = ""
    for i in range(self._max_size):
      if not self._data[i] is None:
        string = string + " [" + str(self._data[i]) + "] "
        if i < self._max_size - 1:
          string = string + "->" 
      else:
        string = string + " [None] "
        if i < self._max_size - 1:
          string = string + "->" 
    return string

  def enqueue(self, value):
    """
    Adds a value to this QueueArray

    This function adds a value to the queue array. If the current size is 
    greater than or equal to the maximum size, the array is re-sized to fit 
    more values into the array

    Parameter value: the value to insert 
    Precondition: value is not None
    """
    # self._data = [18, 12, 33, 4, 5]; value = 3
    if self._size >= self._max_size:
      # if 5 >= 5
      numNones = 5 if self._max_size < 5 else 2 * self._max_size
      self._data = ([None] * numNones) + self._data 
      # self._data = [None, None, None, None, None, 18, 12, 33, 4, 5]
      self._max_size = numNones + self._size
      # self._max_size = 5 + 5 = 10
    self._data[self._max_size - self._size - 1] = value 
    # self._data[10-5-1 => 4] = value 
     # self._data = [None, None, None, None, value, 18, 12, 33, 4, 5]
    self._size += 1

  def queue(self):
    """
    Removes a value from the queue 

    This function removes the first item to be added to the QueueArray. This is 
    equivalent to removing the last item from the array data structure. 
    If the queue pops an empty value, the QueueArray is resized.

    Returns: the value that is removed or None if the QueueArray is empty
    """
    self._max_size -= 1
    self._size -= 1
    value = self._data.pop()
    if value is None:
      self._data = [None] * 5
      self._max_size = 5
    return value

  def peek(self):
    """
    Looks at the first item to be added to the queue. 

    This function returns the first item to be added to the queue, or the last 
    item of the array data structure.

    Returns: the first value to be added to the QueueArray
    """
    return self._data[self._max_size-1]

  def isEmpty(self):
    """
    Returns whether the queue is empty. This is equivalent to returning if the 
    last value of the array data structure is None.

    Returns: True if the queue is empty; False otherwise
    """
    return self._data[self._max_size - 1] is None


    
