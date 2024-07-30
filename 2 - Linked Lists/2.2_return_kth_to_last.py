# Implement an algorithm to find the kth to last element of a singly linked list.

import node_class


def return_kth_to_last(node: node_class.Node, k: int) -> node_class.Node:
    # I don't think it's possible to go backwards if there's no link back, so this is an
    # edge case we need to look out for.

    # Can we assume we start at the beginning?
    if node is None:
        return node_class.Node(0)

    node1: node_class.Node = node
    while k > 0:
        if node1 is None:
            # Out of bounds.
            return node_class.Node(0)

        node1 = node1.next_node
        k -= 1

    node2: node_class.Node = node
    while node1.next_node is not None:
        node2 = node2.next_node
        node1 = node1.next_node

    return node2
