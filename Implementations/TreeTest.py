from Tree import *
# change from Tree to from TreeBlank


def tests():
  print(f"\nTest Trees")
  t = TreeNode(5)
  print("Testing tree height")
  assert t.height() == 1
  t.add_child(10) 
  t.add_child(20) 
  assert t.height() == 2 
  c = t.get_children()[0]
  c.add_child(40)
  c.add_child(10)
  c.add_child(300)
  assert t.height() == 3
  c2 = c.get_children()[2] 
  c2.add_child(-1)
  assert t.height() == 4
  print("Tree height complete")
  print("Tree test complete")
  

