# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes
# greater than or equal to x. (IMPORTANT: The partition element x can appear anywhere in the "right partition";
# it does not need to appear between the left and right partitions.)

import node_class


def partition(node: node_class.Node, partition_value: int) -> node_class.Node:
    head: node_class.Node = node
    tail: node_class.Node = node

    while node is not None:
        if node.data < partition_value:
            node.next_node = head
            head = node
        else:
            tail.next_node = node
            tail = node

        node = node.next_node

    return node
