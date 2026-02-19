#
# Gagnaskipan.
# Deque implementation
# Student(s):
# Guðmundur Alexander Magnússon
# Hafþór Haugen
# Olgeir Otri Engilbertsson

import sll
import dll

class Deque:

    def __init__(self, lst):
        """
        Constructor.
        """
        self.list = lst

    def __len__(self):
        """
        Returns the number of elements in the deque.
        :return: Number of elements.
        """

        return len(self.list)

    def __str__(self):
        """
        Returns the string representation of the deque.
        :return: String representation.
        """
        
        return str(self.list)

    def is_empty(self):
        """
        Returns True if the deque is empty, otherwise False.
        """

        return len(self.list) == 0

    def front(self):

        return self.list.front()

    def back(self):
        
        return self.list.back()

    def append(self, item):
        """
        Inserts the element to the right (top) of the deque.
        :return: None
        """

        self.list.push_back(item)

    def appendleft(self, item):
        """
        Inserts the element to the left (bottom) of the deque.
        :return: None
        """

        self.list.push_front(item)

    def pop(self):
        """
        Removes the element at the right (top) of the deque.
        :return: None. Raises an exception if empty.
        """

        self.list.pop_back()

    def popleft(self):
        """
        Removes the element at the left (bottom) of the deque.
        :return: None. Raises an exception if empty.
        """
        
        self.list.pop_front()

