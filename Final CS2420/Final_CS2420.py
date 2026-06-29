from LinkedList import LinkedList
from Node import Node

#create new class to extend LinkedList
class LinkedListSet(LinkedList):
    def __init__(self):
        super().__init__()

#override append, add, insert if duplicates
#are these items in the set?
    def append(self, item):
        if self.search(item) == False:
            super().append(item)
        
    def add(self, item):
        if self.search(item) == False:
            super().add(item)

    def insert(self, posn, item):
        if self.search(item) == False:
            super().insert(posn, item)

    #len so tester works
    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

#add set operations: union, intersect, difference
    #union- if item is in either of sets
    def union(self, new_set):
        outcome = LinkedListSet()

        current = self.head
        while current is not None:
            if outcome.search(current.data) == False:
                outcome.add(current.data)
            current = current.next

        current = new_set.head
        while current is not None:
            if outcome.search(current.data) == False:
                outcome.add(current.data)
            current = current.next

        return outcome

    #intersect- if an item is in both sets
    def intersect(self, new_set):
        outcome = LinkedListSet()

        current = self.head
        while current is not None:
            if new_set.search(current.data): 
                outcome.add(current.data)
            current = current.next
        return outcome
    
    #difference- if an item only exists in one set
    def difference(self, new_set):
        outcome = LinkedListSet()

        current = self.head
        while current is not None:
            if new_set.search(current.data) == False:
                outcome.add(current.data)
            current = current.next
        return outcome