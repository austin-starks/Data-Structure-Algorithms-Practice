import sys
sys.path.insert(1, "Implementations")
import LinkedListTest
import StackTest
import QueueTest
import TreeTest
import TrieTest


# Curriculum

# Data Structures
# •	Arrays Description: An array is a data structure that stores a collection
# of data; each data point being identified by an index
# -	Big-O for insert: O(n)
# -	Big-O for delete: O(n)
# -	Big-O for lookup: O(1) (O(n) to find the data point, but O(1) if you know index)
# -	Example use: To implement a matrix

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


# •	Binary Search Tree Description:
# -	Big-O for insert:
# -	Big-O for delete:
# -	Big-O for lookup:
# -	Implementation link (include insert and delete):
# -	Example use:

# •	Heap Description:
# -	Big-O for insert:
# -	Big-O for delete:
# -	Big-O for lookup:
# -	Implementation link:
# -	Example use:

# •	Hash Table Description:
# -	Big-O for insert:
# -	Big-O for delete:
# -	Big-O for lookup:
# -	The collision methods are:
# -	Implementation link:
# -	Example use:

# •	Hash Set Description:
# -	Big-O for insert:
# -	Big-O for delete:
# -	Big-O for lookup:
# -	Implementation link:
# -	Example use:

# •	Linked Hash Map Description:
# -	Big-O for insert:
# -	Big-O for delete:
# -	Big-O for lookup:
# -	Implementation link:
# -	Example use:


# Algorithms (give implementation links)
# •	Trees
# -	Preorder traversal:
# -	Inorder traversal:
# -	Postorder traversal

# •	Sorting
# -	Insertion sort
# -	Selection sort
# -	Quick sort
# -	Merge sort
# -	Bubble sort

# •	Graphs
# -	A* Search (CS 4700)
# -	Dijkstra’s
# -	BFS (when to use BFS over DFS – CS 4700)
#   	Include recursive and non-recursive implementations
# -	DFS (when to use DFS over BFS)
#   	Include recursive and non-recursive implementations


# Miscellaneous (can be done after leetcode)
# -	What is amortized constant-time?
# -	What is HTTP?
# -	How do sockets work?
# -	What is IP?
# -	What are the networking layers?



if __name__ == '__main__':
    LinkedListTest.tests()
    StackTest.tests()
    QueueTest.tests()
    TreeTest.tests()
    TrieTest.tests()
    
