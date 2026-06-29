from Node import Node
class LinkedList:
    """A list of (non-sorted) items"""

    def __init__(self):
        self.head = None

    def __str__(self):
        if(self.head == None):
            return "[]"
        elif self.head.next == None:
            return "["+self.head.data+"]"
        else:
            s = "["+self.head.data
            current = self.head.next
            while current is not None:
                s += ", "+ current.data
                current = current.next
            s += "]"
            return s


    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        """This method adds item to the end of the list"""
        if self.head == None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)

    def index(self, item):
        """This method returns the position of item in the list or raises a ValueError"""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError("Item not in list")
    
    def insert(self, posn, item):
        """adds a new item to the list at position posn or raises a ValueError."""
        if posn == 0:
            tmp = Node(item)
            tmp.next = self.head
            self.head = tmp
        else:
            current = self.head
            index = 0
            while current.next is not None:
                if(index == posn-1):
                    tmp = Node(item)
                    tmp.next = current.next
                    current.next = tmp
                    return
                else:
                    current = current.next
                    index += 1
            if index == posn-1:
                current.next = Node(item)
            else:
                raise ValueError("posn is out of bounds")

    def pop(self):
        """removes and returns the last item in the list or raises a ValueError"""
        if self.head is None:
            raise ValueError("Unable to pop from an empty list")
        else:
            tmp = self.head.data
            self.head = self.head.next
            return tmp        
        pass

    def pop_at_position(self, posn):
        """removes and returns the item at position posn or raises a ValueError."""
        if self.head is None:
            raise ValueError("Unable to pop from an empty list")
        if posn == 0:
            tmp = self.head.data
            self.head = self.head.next
            return tmp
        else:
            current = self.head
            index = 0
            while current.next is not None:
                if(index == posn-1):
                    if current.next is None:
                        raise ValueError("posn is out of bounds")
                    else:
                        tmp = current.next.data
                        current.next = current.next.next
                        return tmp
                else:
                    current = current.next
                    index += 1
            raise ValueError("posn is out of bounds")

