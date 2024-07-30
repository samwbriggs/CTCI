# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP - How would you solve this problem if a temporary buffer is not allowed?

import node_class


def remove_dups(node: node_class.Node) -> node_class.Node:
    # What am I given as input? A head node?
    # Is it a singly linked list or doubly linked list?

    int_hash: dict[int, int] = {}
    prev_node: node_class.Node
    while node.next_node is not None:
        if node.data not in int_hash:
            int_hash[node.data] = 1
            prev_node = node
        else:
            prev_node.next_node = node.next_node

        node = node.next_node

    # At this point we are at the last node. Check the hash table.
    if node.data in int_hash:
        prev_node.next_node = None
        return prev_node

    return node
