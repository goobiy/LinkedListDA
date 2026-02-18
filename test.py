from sll import SLList
from sll_node import Node
from iterator import NodeIterator
from dll import Position, DLList


l = DLList()


pos_0 = Position(l.tail)
# pos_1 = Position(l.head)  WTF ??

l.insert_before(pos_0,25)
# pos_2 = l.insert_before(pos_1,"Sigma")
# print(l)
# pos_3 = l.insert_before(pos_1,"Sigma_W")
# l.insert_before(pos_2,"Yippy")
# print(l)
# l.insert_before(head_pos,"Olgeur")
# for i in range(10):
#     l.insert_before(head_pos,i)

# print(l)

# print(l.get_at(head_pos))


print(pos_0.node is l.head, pos_0.node is l.tail)
print(pos_0.node.prev)
print(pos_0.node.item)



################################################################################
# l = SLList()

# l.push_back(10)
# l.push_front(40)
# l.push_back(100)
# l.push_front(60)
# l.push_back(25)

# print(l)
# print(l.front())
# print(l.back())

# print("-"*100)


# l.pop_front()
# print(l)
# print(l.front())

# l.pop_back()
# print(l)
# print(l.back())

# print(l._head.next)
