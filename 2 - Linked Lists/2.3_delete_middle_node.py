# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node,
# not necessarily the exact middle) of a singly linked list, given only access to that node.

import node_class


def delete_middle_node(node: node_class.Node) -> None:
    if node is None or node.next_node is None:
        return

    next_node = node.next_node
    node.data = next_node.data
    node.next_node = next_node.next_node
