class LinkedListNode(object):
    """
    A node for a Singly Linked List

    This node is used to implement a LinkedList. It contains the data and 
    a pointer to the next node.

    Class invariants: 
        - self.data:     the data to store in the LinkedList 
        - self.next: the Node this Node points to
    """
    def __str__(self):
        """
        Returns: The string representation of this Node
        """
        return "[" + str(self.data) + "]"

    
    def __init__(self, data):
        """
        Initalizes a node for a Linked List

        This Node stores data and also the next node
        
        Class invariants: 
            - self.data:     the data to store in the LinkedList 
            - self._nextNode: the Node this Node points to
        """
        self.data = data
        self.next = None

    def setNextNode(self, node):
        """
        Sets the next node to be node

        This function changes the next Node to be node

        Parameter node: the node to set to be this node's next node.
        """
        if isinstance(node, LinkedListNode) or node is None:
            self.next = node
        else:
            self.next = LinkedListNode(node)


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
        if isinstance(head, LinkedListNode):
            self._head = head
        else:
            self._head = LinkedListNode(head) 
        self._size = 1

    def __str__(self):
        """
        Returns: the string representation of the linked list
        """
        currentNode = self._head
        string = ""
        while currentNode != None:
            string += str(currentNode)
            currentNode = currentNode.next
            if currentNode != None:
                string += " -> "
        return string

    
    def insert(self, data):
        """
        Adds a new data value to the linked list

        This function creates a new node and adds it to the beginning of the 
        Linked List.

        Parameter data: the data to add 
        """
        if isinstance(data, LinkedListNode):
            newNode = data 
        else:
            newNode = LinkedListNode(data)
        newNode.setNextNode(self._head)
        self._head = newNode
        self._size += 1

   
    def size(self):
        """
        Returns: the size of the linked list
        """
        return self._size

   
    def find(self, value):
        """
        Finds the first node that has value on its data. 

        This function iterates through the Linked List to find a node with 
        value in its data. If it doesn't exist, this function returns None.

        Returns: the LinkedListNode with value as its data or None 
        """
        currentNode = self._head
        while currentNode != None and currentNode.data != value:
            currentNode = currentNode.next
        if currentNode is None:
            return None
        else:
            return currentNode

    
    def delete(self, value):
        """
        Deletes the value from the linked list

        This function iterates through the linked list and deletes the first 
        node with value in its data. 
        """
        currentNode = self._head
        prevNode = None
        while currentNode != None and currentNode.data != value:
            prevNode = currentNode
            currentNode = currentNode.next
        if currentNode == None:
            return
        else:  # that means currentNode == value
            if prevNode == None:  # that means the first item is deleted
                self._head = currentNode.next
            else:
                prevNode.setNextNode(currentNode.next)
            self._size -= 1
