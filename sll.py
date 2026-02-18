#
# Gagnaskipan.
# Single-Linked-List
# Student(s):
#  Guðmundur A. Magnússon
#  Hafþór Haugen
#  Olgeir Otri Engilbertsson

from sll_node import Node
from iterator import NodeIterator

class SLList:

    def __init__(self):
        """
        Constructor.
        Time complexity: O(1)
        """
        self._head = None
        self._tail = None
        self._len = 0

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        return NodeIterator(self._head)

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        elems = []
        node = self._head
        while node is not None:
            elems.append(str(node.item))
            node = node.next
        return '[' + ', '.join(elems) + ']'

    def __len__(self):
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """
        return self._len

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        return self._head is None  # could alternatively check _tail is None, or _len is 0.

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError('front called on an empty list')
        return self._head.item

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError('back called on an empty list')
        return self._tail.item

    def push_front(self, item) -> None:
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        old_front = self._head
    
        new_node = Node(item, old_front)

        self._head = new_node

        if self._len == 0:
            self._tail = new_node

        self._len += 1
        return

    def pop_front(self) -> None:
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self._head is None:
            raise IndexError("The SLL is empty")
        
        self._head = self._head.next

        self._len -= 1

        if self._head is None:
            self._tail = None
        return

    def push_back(self, item) -> None:
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        
        old_back = self._tail

        new_node = Node(item, None)
        if self._len != 0:
            old_back.next = new_node

        self._tail = new_node

        if self._len == 0:
            self._head = new_node

        self._len += 1
        return

    def pop_back(self) -> None:
        """
        Remove an element from the back of the list.
        Time complexity: O(n)
        :return: None, but trows an exception if list empty.
        """
        if self._tail is None:
            raise IndexError("The SLL is empty")
        
        if self._head is self._tail:
            self._head = None
            self._tail = None
            self._len = 0
            return

        current_node = self._head
        # Iterating towards the last element in the SLL
        while current_node.next != self._tail:
            current_node = current_node.next

        
        current_node.next = None
        self._tail = current_node
        self._len -= 1
        return