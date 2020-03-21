class QueueArray(object):
  """
  Implementation of Queue using an array. 
  """
  def __init__(self, value=None):
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
    Adds a value to a queue
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
    self._size += 1

  def queue(self):
    """
    Removes a value from the queue and returns the remove value
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
    Returns the first 
    """
    return self._data[self._max_size-1]

  def isEmpty(self):
    """
    Returns: true if the queue is empty; false otherwise
    """
    return self._data[self._max_size - 1] is None


    
