# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node,
# not necessarily the exact middle) of a singly linked list, given only access to that node.

import node_class


def delete_middle_node(node: node_class) -> None:
    if node is None or node.nextNode is None:
        return

    next_node = node.nextNode
    node.data = next_node.data
    node.nextNode = next_node.nextNode
