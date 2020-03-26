import sys
sys.path.insert(1, "implementations_python")
import LinkedListTest
import StackTest
import QueueTest
import TreeTest
import TrieTest
import BSTTest


# Curriculum

# Data Structures
# •	Linked List Description: A collection of data whose order is given by the
# element it points to. Each node point contains data and the next value
# -	Big-O for insert: O(1) (to insert; looking up is still O(n) )
# -	Big-O for delete: O(1)
# -	Big-O for lookup: O(n)
# -	Example use: An image viewer that loads the next and previous image or a
#  web browser's back/forward button. Also, a music player. Can also be used
#  to implement a stack/queue (doubly linked).
# -	Implementation: LinkedList.py

# •	Stack Description: A data type that holds a collection of elements that can
# only be accessed by adding and removing from the top of the stack (LIFO). 
# They support push and pop. A stack is used for DFS.
# -	Big-O for insert: O(1)
# -	Big-O for delete: O(1)
# -	Big-O for lookup: O(n)
# -	Example use: DFS
# -	Implementation link (include pop and push): Stack.py

# •	Queue Description: A data type that holds a collection of elements that can 
#   only be accessed by adding from the top and removing from the buttom (FIFO)
# -	Big-O for insert: O(1)
# -	Big-O for delete: O(1)
# -	Big-O for lookup: O(n)
# -	Example use: BFS
# -	Implementation link (include queue and enqueue): Queue.py

# •	Tree Description: An undirected acyclic graph. A tree is a node that has 
#   children that are also nodes.
# -	Tree height definition: The length of the longest downward path to a leaf 
#                           from a root node
# -	Tree depth definition: The length of the path to its root
# - Implementation link: Tree.py

# •	Trie Description: A tree that can effeciently store words. It allows 
#   one to effeciently store words, especially words in which a lot of them 
#   start with the same letter.
# -	Big-O for insert: O(n) (length of the key you're storing)
# -	Big-O for delete: O(n) (faster if you want to delete all words with a certain
#                     prefix)
# -	Big-O for lookup: O(n)
# - Example use: creating an operating system; the folders are nodes and the 
# - the data is a list of files. Or storing large genomes in whih you don't have 
#   a lot of space.
# -	Implementation link: Trie.py

# •	Binary Search Tree Description: A binary tree data structure that has a 
#   property that from a given node, every node with a value less than that node 
#   is in the left child, and every node with a value greater than that node is 
#   in the right child.
# -	Big-O for insert: O(log n)
# -	Big-O for delete: O(log n)
# -	Big-O for lookup: O(log n)
#   Preorder: processing the root before the two children 
#   Inorder: processing the left child, the root, then the right child
#   Postorder: processing the children than the root node
# -	Implementation link (include insert and delete): BST.py (TODO - Delete)
# -	Example use: Wanting a data structure to keep things in a sorted order



if __name__ == '__main__':
    LinkedListTest.tests()
    StackTest.tests()
    QueueTest.tests()
    TreeTest.tests()
    TrieTest.tests()
    BSTTest.tests()

    
