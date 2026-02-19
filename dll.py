#
# Gagnaskipan.
# Double-Linked-List
# Student(s):
#  Hafþór Haugen, Guðmundur Alex Magnússon og Olgeir Otri Engilbertsson
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

    def __init__(self) -> None:
        self.head = Node()
        self.tail= Node()

        self.head.next = self.tail
        self.tail.prev = self.head

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

        elems = []
        node = self.head
        while node is not None:
            if node.item is None:
                node = node.next
                continue
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

        return pos.node.item


    def insert_after(self, pos: Position, item: object) -> Position:
        """
        Insert element following position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        original = self.__validator(pos)

        return self.__insert_beween(original, item, original.next)

    

    def insert_before(self, pos: Position, item: object) -> Position:
        """
        Insert element before position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        original = self.__validator(pos)

        return self.__insert_beween(original.prev, item, original)

    def remove(self, pos: Position) -> object:
        """
        Remove element at position 'pos' in the list.
        :param pos: Position of element to remove.
        :return: Element deleted
        """
        self.__validator(pos)
        
        node_to_delete = pos.node

        prev_node = node_to_delete.prev
        next_node = node_to_delete.next

        prev_node.next = next_node
        next_node.prev = prev_node
        node_to_delete.prev = None
        node_to_delete.next = None


        self.size -= 1
        return node_to_delete.item

    def replace(self, pos: Position, item: object) -> object:
        """
        Replace element at position 'pos' in the list.
        :param pos: Position of element to replace
        :param item: New element to replace the existing one.
        :return: The element replaced (formerly at position)
        """
        old_item = pos.node.item

        pos.node.item = item

        return old_item

    def front_pos(self) -> Position | None:
        """
        Return position of the element at the head of the list if list non-empty, or None if list is empty.
        """
        if self.size == 0:
            return None
        return Position(self.head.next)


    def back_pos(self) -> Position | None:
        """
        Return position of the element at the end of list if list non-empty, or None if list is empty.
        """
        if self.size == 0:
            return None
        return Position(self.tail.prev)
        
    def prev_pos(self, pos: Position) -> Position | None:
        """
        Return position before 'pos', or None if already at front of list.
        """
        prev_node = pos.node.prev
        
        if prev_node is None:
            return None

        return Position(prev_node)

    def next_pos(self, pos: Position) -> Position | None:
        """
        Return position following 'pos', or None if already at end of list.
        """
        next_node = pos.node.next

        if next_node is None:
            return None
        
        return Position(next_node)

    def __make_position(self, node: Node):
        if node is self.head or node is self.tail:
            return None
        return Position(node)

    def __insert_beween(self, predecessor: Node, item, successor: Node):

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
        if self.is_empty():
            raise IndexError("The DLL is empty")
        return self.head.next.item

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError("The DLL is empty")
        return self.tail.prev.item

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        head_pos = Position(self.head)

        self.insert_after(head_pos, item)

    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError("The list is empty")
        
        self.remove(Position(self.head.next))

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        tail_pos = Position(self.tail)

        self.insert_before(tail_pos, item)


    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError("The list is empty")
        
        tail_pos = Position(self.tail.prev)

        self.remove(tail_pos)