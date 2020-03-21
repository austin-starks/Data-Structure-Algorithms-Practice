class Node(object):
    def __str__(self):
        return "[" + str(self._data) + "]"

    
    def __init__(self, data):
        """
        Initalizes a node 
        """
        self._data = data
        self._nextNode = None

    
    def getData(self):
        """
        Returns the data in the node
        """
        return self._data

    
    def getNextNode(self):
        """
        Returns the next node
        """
        return self._nextNode

    
    def setNextNode(self, node):
        """
        Sets the next node to be node
        """
        if isinstance(node, Node) or node is None:
            self._nextNode = node
        else:
            self._nextNode = Node(node)


class LinkedList(object):
    def __str__(self):
        """
        Prints the string representation of the linked list. Used for printing
        """
        currentNode = self._head
        string = ""
        while currentNode != None:
            string += str(currentNode)
            currentNode = currentNode.getNextNode()
            if currentNode != None:
                string += " -> "
        return string


    def __init__(self, head=None):
        """
        Initializes a linked list
        """
        if isinstance(head, Node):
            self._head = head
        else:
            self._head = Node(head) 
        if head==None:
            self._size = 0 
        else:
            self._size = 1

    
    def insert(self, data):
        """
        Adds a new data value to the linked list
        """
        newNode = Node(data)
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
        Returns: the node with value 
        """
        currentNode = self._head
        while currentNode != None and currentNode.getData() != value:
            currentNode = currentNode.getNextNode()
        if currentNode is None:
            return None
        else:
            return currentNode

    
    def delete(self, value):
        """
        Deletes the value from the linked list
        """
        currentNode = self._head
        prevNode = None
        while currentNode != None and currentNode.getData() != value:
            prevNode = currentNode
            currentNode = currentNode.getNextNode()
        if currentNode == None:
            return
        else:  # that means currentNode == value
            if prevNode == None:  # that means the first item is deleted
                self._head = currentNode.getNextNode()
            else:
                prevNode.setNextNode(currentNode.getNextNode())
            self._size -= 1
