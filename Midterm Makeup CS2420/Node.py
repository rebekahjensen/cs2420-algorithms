class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    @property
    def data(self):
        """The data stored in the node"""
        return self._data

    @data.setter
    def data(self, node_data):
        self._data = node_data

    @property
    def next(self):
        """The next node"""
        return self._next

    @next.setter
    def next(self, node_next):
        self._next = node_next

    def __str__(self):
        """String"""
        return str(self._data)
    
    def __eq__(self, node_next):
        return type(node_next) is Node and self.data == node_next.data