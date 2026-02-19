#
# Gagnaskipan.
# Deque implementation
# Student(s):
# Guðmundur Alexander Magnússon
# Hafþór Haugen
# Olgeir Otri Engilbertsson

import sll
import dll

class Queue:

    def __init__(self, lst):
        """"
        Constructor.
        """

        self.list = lst

    def __len__(self):
        """"
        Returns the number of elements in the queue.
        """
        
        return len(self.list)

    def __str__(self):
        """
        Returns the string representation of the queue.
        """
        
        return str(self.list)

    def is_empty(self):
        """
        Returns True if queue is empty, otherwise False.
        """

        return len(self.list) == 0

    def front(self):
        """
        Returns the front element of the queue (without removing it).
        :return: If non-empty, the front element of the queue, otherwise throws exception.
        """

        if len(self.list) == 0:
            raise IndexError("Queue is empty")
        
        return self.list.front()

    def enqueue(self, item):
        """
        Inserts the element to the back of the queue.
        """

        self.list.push_back(item)

    def dequeue(self):
        """
        Removes the element at the front of the queue (without returning)..
        """

        self.list.pop_front()