#
# Gagnaskipan.
# Double-Linked-List
# Student(s):
#  Hafþór Haugen og Guðmundur Alex Magnússon
#
from dll_node import Node
from iterator import NodeIterator


class Position:
    __slots__ = ['node']

    def __init__(self, node):
        self.node = node


class DLList:

    #
    # Beginning of fundamental section.
    #

    def __init__(self):
        self.head = Node()
        self.tail= Node()
        #Erum currently með sentinal nodes, held ég amk.
        self.head.next = self.tail

        self.tail.prev = self.head

        self.current = self.tail    # þarf ?
        self.size = 0
        self.position = Position(self.head)

    def __iter__(self) -> None:
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        return NodeIterator(self.head)
    
    def __str__(self) -> str:
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """

        elems = []      # má þetta ?
        node = self.head
        while node is not None:
            elems.append(str(node.item))
            node = node.next
        return '[' + ', '.join(elems) + ']'

    def __len__(self) -> int:
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """

        return self.size

    def is_empty(self) -> bool:
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """

        return self.size == 0

    def get_at(self, pos: Position) -> object:
        """
        Return element at position 'pos'.
        :param pos: Position to insert
        :return: Element
        """
        # if self.size == 0:
        #     raise IndexError("DLL is empty")
        # if pos.node.item is None:   # ??
        #     raise IndexError("Nothing there")
        
        return pos.node.item


    def insert_after(self, pos: Position, item: object) -> Position:
        """
        Insert element following position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        
        # left_node = self.get_at(pos)
        # the_right_one = left_node.next

        # new_node = Node(item)
        
        # left_node.next = new_node

        # new_node.prev = left_node
        # new_node.next = the_right_one

        # the_right_one.prev = new_node
        original = self.__validator(pos)
        #return self.__insert_beween(item,original.prev, original) #Sennilega vitlaus notkun

        return self.__insert_beween(item,original,original.next) #Sennilega vitlaus notkun

    

    def insert_before(self, pos: Position, item: object) -> Position:
        """
        Insert element before position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        original = self.__validator(pos)
        #return self.__insert_beween(item,original.prev, original) #Sennilega vitlaus notkun

        return self.__insert_beween(item,original.prev,original) #Sennilega vitlaus notkun

    def remove(self, pos: Position) -> object:
        """
        Remove element at position 'pos' in the list.
        :param pos: Position of element to remove.
        :return: Element deleted
        """
        ...
        return None

    def replace(self, pos: Position, item: object) -> object:
        """
        Replace element at position 'pos' in the list.
        :param pos: Position of element to replace
        :param item: New element to replace the existing one.
        :return: The element replaced (formerly at position)
        """
        ...
        return None

    def front_pos(self) -> Position | None:
        """
        Return position of the element at the head of the list if list non-empty, or None if list is empty.
        """
        ...
        return None

    def back_pos(self) -> Position | None:
        """
        Return position of the element at the end of list if list non-empty, or None if list is empty.
        """
        ...
        return None

    def prev_pos(self, pos: Position) -> Position | None:
        """
        Return position before 'pos', or None if already at front of list.
        """
        ...
        return None

    def next_pos(self, pos: Position) -> Position | None:
        """
        Return position following 'pos', or None if already at end of list.
        """
        ...
        return None

    def __make_position(self, node: Node):
        if node is self.head or node is self.tail:
            return None
        return Position(node)

    def __insert_beween(self, item, predecessor: Node, successor: Node):

        new_node = Node(predecessor, item, successor)

        new_node.prev = predecessor
        new_node.next = successor

        successor.prev = new_node
        predecessor.next = new_node

        

        self.size += 1
        return self.__make_position(new_node)
    
    def __validator(self, pos: Position) -> Node:

        if not isinstance(pos, Position):
            raise TypeError("the position must me a Position type")
        
        # if pos.container is not self:
        #     raise ValueError("the position does not belong to this container")
        
        if pos.node is None:
            raise ValueError("the position is no longer valid")
        
        return pos.node


    #
    # End of fundamental section.
    # Implement the methods below by, for the most part, using/calling the ones you have implemented above.
    # Avoid unnecessary code duplication.
    #

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        ...
        return None

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        ...
        return None

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        ...

    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        ...

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        ...

    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        ...
