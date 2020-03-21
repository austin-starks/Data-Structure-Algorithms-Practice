from Stack import * 
# change from Stack to from StackBlank


def tests():
  print("\nTesting LinkedList stack")
  s = LinkedListStack(5)
  print("Testing peek")
  assert s.peek()==5, "Peek should be 5"
  print("Peek test complete")
  print("Testing size")
  assert s.size()==1, "Size should be 1"
  print("Size test complete")
  print("Testing push")
  s.push(7)
  assert s.peek() == 7, "Top element should be 7" 
  print("Push test complete") 
  print("Testing pop")
  s.pop()
  assert s.peek() == 5, "Top element should be 5" 
  print("Pop test complete") 
  print("Test isEmpty")
  assert s.isEmpty() == False, "isEmpty should be False"
  s.pop()
  assert s.isEmpty() == True, "isEmpty should be True"
  print("isEmpty test is complete")
  print("Linked List Stack tests complete\n")

  print("\nTesting LinkedList Array")
  s = LinkedListArray(5)
  print("Testing peek")
  assert s.peek()==5, "Peek should be 5"
  print("Peek test complete")
  print("Testing size")
  assert s.size()==1, "Size should be 1"
  print("Size test complete")
  print("Testing push")
  s.push(7)
  assert s.peek() == 7, "Top element should be 7" 
  print("Push test complete") 
  print("Testing pop")
  val = s.pop()
  assert val == 7, "Should have popped 7"
  assert s.peek() == 5, "Top element should be 5" 
  print("Pop test complete") 
  print("Test isEmpty")
  assert s.isEmpty() == False, "isEmpty should be False"
  s.pop()
  assert s.isEmpty() == True, "isEmpty should be True"
  print("isEmpty test is complete")
  print("Linked List tests complete\n")