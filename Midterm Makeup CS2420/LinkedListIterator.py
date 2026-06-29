from Node import Node
from LinkedList import LinkedList

class LinkedListIterator:
    """An iterator for the LinkedList class"""

    #if not linkedlist, valueerror
    #assign variables
    def __init__(self, list):
        if type(list) is not LinkedList:
            raise ValueError()
        self.current_node = list.head
        self.my_list = list

    #return num of nodes in list
    def size_of_list(self):
        return self.my_list.size()

    #return first node in list
    #if no nodes in list, return none
    def get_beginning_node(self):
        if self.my_list.head == None:
            return None
        return self.my_list.head
        
    #return last node in list
    #if no nodes, return none
    def get_ending_node(self):
        current  = self.my_list.head
        if current == None:
            return None

        while current.next:
            current = current.next
        return current

    #return node in current location
    #return none if no nodes
    def get_node_at_current_location(self):
        return self.current_node
        #return 5 #This is just so the tester breaks

    #make current location in list
    #raise indexerror if out of list
    def advance_to_next_node(self):
        if self.current_node.next == None:
            raise IndexError("Index is out of range")
        
        self.current_node = self.current_node.next

    #true if nodes after current node
    #false otherwise
    def has_next_node(self):
        if self.current_node == None or self.current_node.next == None:
            return False
        return True

    #previous current
    #raise indexerror if before list
    def go_back_a_node(self):
        if self.current_node == None:
            raise IndexError("Index is out of range")
    
        if self.current_node == self.my_list.head:
            raise IndexError("Index is out of range")
        current = self.my_list.head
        
        while current.next != self.current_node:
            current = current.next
        self.current_node = current

    #true if nodes before current node
    # #false otherwise    
    def has_previous_node(self):
        if self.current_node != self.my_list.head:
            return True
        return False