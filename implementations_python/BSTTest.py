from BST import *
# change from Trie to from TreeBlank
# This website was helpful for testing:
# http://www.cs.armstrong.edu/liang/animation/web/BST.html


def tests():
  print("\nTest Binary Search Tree")
  print("Test insert and find")
  bst = BinarySearchTree(100) # root = 100

  bst.insert(50) 
  bst.insert(50) # note: added twice for force_delete
  bst.insert(150)

  bst.insert(25) #note: added twice 
  bst.insert(25)
  bst.insert(75)
  bst.insert(125)
  bst.insert(175)

  bst.insert(10)
  bst.insert(30)
  bst.insert(60)
  bst.insert(90)
  bst.insert(110)
  bst.insert(130)
  bst.insert(160)
  bst.insert(200)

  bst.insert(0)
  bst.insert(15)
  bst.insert(27)
  bst.insert(33)
  bst.insert(55)
  bst.insert(70)
  bst.insert(80)
  bst.insert(95)
  bst.insert(105)
  bst.insert(115)
  bst.insert(127)
  bst.insert(133)
  bst.insert(155)
  bst.insert(165)
  bst.insert(190)
  bst.insert(205)
  assert bst.find(50) == 2, f"received result: {bst.find(50)}"
  assert bst.find(25) == 2, f"received result: {bst.find(50)}"
  assert bst.find(0) == 1, f"received result: {bst.find(1)}"
  assert bst.find(205) == 1, f"received result: {bst.find(1)}"
  assert bst.find(95) == 1, f"received result: {bst.find(1)}"
  assert bst.find(70) == 1, f"received result: {bst.find(1)}"
  assert bst.find(55) == 1, f"received result: {bst.find(1)}"
  assert bst.find(500) == 0, f"received result: {bst.find(500)}"
  assert bst.find(-500) == 0, f"received result: {bst.find(500)}"
  print("Test insert and find complete")
  print("Test inorder, preorder, and postorder")
  assert bst.inorder() == [0, 10, 15, 25, 27, 30, 33, 50, 55, 60, 70, 75, 80, 
                          90, 95, 100 ,105, 110, 115, 125 ,127, 130, 133, 150, 
                          155, 160, 165, 175, 190, 200, 205], f"Obtained result: {bst.inorder()}"
  assert bst.preorder() == [100, 50, 25, 10, 0, 15, 30, 27, 33, 75, 60, 55, 70, 
                            90, 80, 95, 150, 125, 110, 105, 115, 130, 127, 133, 
                            175, 160, 155, 165, 200, 190, 205], f"Obtained result: {bst.preorder()}"
  assert bst.postorder() == [0, 15, 10, 27, 33, 30, 25, 55, 70, 60, 80, 95, 90, 
                            75, 50, 105, 115, 110, 127, 133, 130, 125, 155, 165, 
                            160, 190, 205, 200, 175, 150, 100], f"Obtained result: {bst.postorder()}"
  print("Traversal tests complete")

  print("Binary Search Tree test complete\n")
  
  


