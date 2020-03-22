class Node(object):
    """
    A node for a Singly Linked List

    This node is used to implement a LinkedList. It contains the data and 
    a pointer to the next node.

    Class invariants: 
        - self._data:     the data to store in the LinkedList 
        - self._nextNode: the Node this Node points to
    """

    def __init__(self, data, next_node=None):
        """
        Initalizes a node for a Linked List

        This Node stores data and also the next node
        
        Class invariants: 
            - self._data:     the data to store in the LinkedList 
            - self._nextNode: the Node this Node points to
        """
        pass

    
    def getData(self):
        """
        Returns: the data in this LinkedListNode
        """
        pass

    
    def getNextNode(self):
        """
        Returns: the node stored in the next node.
        """
        pass

    
    def setNextNode(self, node):
        """
        Sets the next node to be node

        This function changes the next Node to be node

        Parameter node: the node to set to be this node's next node.
        """
        pass


class LinkedList(object):
    """
    A class representing a linked list.

    This class implements a linked list, including functions such as insert, 
    delete, size, and find.

    Class invariants:
        - self._head: the node at the head of the LinkedList.
        - self._size: the size of the LinkedList
    """
    def __init__(self, head=None):
        """
        Initializes a linked list

        A linked list is a structure that contains a head that is a LinkedListNode 
        and a size attribute.

        Class invariants:
            - self._head: the node at the head of the LinkedList.
            - self._size: the size of the LinkedList        
        """
        pass

    
    def insert(self, data):
        """
        Adds a new data value to the linked list

        This function creates a new node and adds it to the beginning of the 
        Linked List.

        Parameter data: the data to add 
        """
        pass

   
    def size(self):
        """
        Returns: the size of the linked list
        """
        pass

   
    def find(self, value):
        """
        Finds the first node that has value on its data. 

        This function iterates through the Linked List to find a node with 
        value in its data. If it doesn't exist, this function returns None.

        Returns: the LinkedListNode with value as its data or None 
        """
        pass

    
    def delete(self, value):
        """
        Deletes the value from the linked list

        This function iterates through the linked list and deletes the first 
        node with value in its data. 
        """
        pass
