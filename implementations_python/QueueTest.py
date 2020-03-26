from Queue import *
# change from Queue to from QueueBlank


def tests():
  q = QueueArray(1)
  print("\nTesting queues")
  # print(f"Initial queue: {q}")
  print(f"Testing peek")
  assert q.peek() == 1, "Peek should be 1"
  q.enqueue(4)
  assert q.peek() == 1, "Peek should be 1" 
  print("Test peek complete")
  print("Test enqueue")
  # print(f"Queue after enqueue 4: {q}")
  q.enqueue(7)
  # print(f"Queue after enqueue 7: {q}")
  print("Test enqueue complete")
  print("Test queue")
  assert q.queue() == 1,"Queue should return 1"
  # print(f"Queue after queue function: {q}")
  assert q.queue() == 4,"Queue should return 4"
  # print(f"Queue after queue function again: {q}")
  print("Test isEmpty")
  assert q.isEmpty() == False
  q.enqueue("Bye")
  q.enqueue("Hi")
  q.enqueue(40)
  q.enqueue(3)
  q.enqueue(10)
  # print(f"Queue after adding 5 elements {q}")
  assert q.queue() == 7 
  # print(f"Queue after removing 1 element {q}")
  a = q.queue()
  assert a == "Bye"
  # print(f"Queue after removing 1 element {q}")
  assert q.queue() == "Hi"
  assert q.queue() == 40
  assert q.queue() == 3
  # print(f"Queue after removing 3 more elements {q}")
  assert q.isEmpty() == False
  assert q.queue() == 10
  assert q.isEmpty() == True
  # print(f"Queue after removing 1 more elements {q}")
  assert q.queue() == None
  assert q.isEmpty() == True
  # print(f"Queue after removing 1 more elements {repr(q)}")
  print("isEmpty test complete")
  print("Queue test complete\n")

