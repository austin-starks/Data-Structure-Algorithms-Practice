from LinkedList import *
# change from LinkedList to from LinkedListBlank

def tests():
    print("\nTesting linked lists")
    l = LinkedList(1)
    # print("Starting linked list", l)
    l.insert(5)
    l.insert(6)
    l.insert(7)
    # print(l)
    # print("Linked list after inserting 5,6,7:", l)
    print("Test size")
    assert l.size() == 4, "The size should be 4"
    print("Size test Complete")
    print("Test find")
    node = l.find(5)
    assert node.getData() == 5, "The node should be 5"
    node = l.find(1)
    assert node.getData() == 1, "The node should be 1"
    node = l.find(8)
    assert node == None, "The node should be None"
    print("Find test complete")
    print("Test delete")
    # print("linked list before deleting:", l)
    l.delete(6)
    assert l.find(6) == None, "6 should've been deleted"
    l.delete(1)
    assert l.find(1) == None, "1 should've been deleted"
    l.delete(5)
    assert l.find(5) == None, "5 should've been deleted"
    print("Delete test complete")
    print("Linked List tests complete\n")
    # print("Linked list after deleting 6, 1, and 5:", l)
