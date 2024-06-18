# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP - How would you solve this problem if a temporary buffer is not allowed?

import node_class


def remove_dups(node: node_class.Node) -> node_class.Node:
    # What am I given as input? A head node?
    # Is it a singly linked list or doubly linked list?

    intHash: dict[int] = {}
    prevNode: node_class.Node
    while node.nextNode != None:
        if not node.data in intHash:
            intHash[node.data] = 1
            prevNode = node
        else:
            prevNode.nextNode = node.nextNode

        node = node.nextNode

    # At this point we are at the last node. Check the hash table.
    if node.data in intHash:
        prevNode.nextNode = None
        return prevNode

    return node
