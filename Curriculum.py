import sys
sys.path.insert(1, "Implementations")
import LinkedListTest
import StackTest
import QueueTest


# Curriculum

# Data Structures
# •	Arrays Description: An array is a data structure that stores a collection
# of data; each data point being identified by an index
# -	Big-O for insert: O(n)
# -	Big-O for delete: O(n)
# -	Big-O for lookup: O(1)
# -	Example use: To implement a matrix


# •	Linked List Description: A collection of data whose order is given by the
# element it points to. Each node point contains data and the next value
# -	Big-O for insert: O(1) (to insert; looking up is still O(1)
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
# -	Implementation link (include pop and push): Stack.py
# -	Example use: DFS


# •	Queue Description: A data type that holds a collection of elements that can 
#   only be accessed by adding from the top and removing from the buttom (FIFO)
# -	Big-O for insert: O(1)
# -	Big-O for delete: O(1)
# -	Big-O for lookup: O(n)
# -	Implementation link (include queue and enqueue): Queue.py
# -	Example use: BFS


# •	Tree Description:
# -	Tree height definition:
# -	Tree depth definition:
# -	Big-O for insert:
# -	Big-O for delete:
# -	Big-O for lookup:
# -	Implementation link:

# •	Trie Description:
# -	Big-O for insert:
# -	Big-O for delete:
# -	Big-O for lookup:
# -	Implementation link:

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
    
