# Implement a function to check if a linked list is a palindrome.

import node_class

def palindrome(node: node_class.Node):
    # If we knew the size of the list this would be a piece of cake.
    # Using a hash table to track occurrence of letters would always work well - but it would be pretty high space complexity.

    first_half: node_class.Node = node_class.Node(0)
    pointer: node_class.Node = node

    while pointer.next_node.next_node is not None:
        # Fast forward to the middle of the list while tracking the first half of the elements.
        pointer = pointer.next_node.next_node

        current_list: node_class.Node = first_half
        first_half = node_class.Node(node.data)
        first_half.next_node = current_list
        node = node.next_node

    if pointer.next_node is None:
        # There is an odd number of elements in this linked list. It does not matter what the middle element is. Skip it!
        node = node.next_node
    else:
        # Add the final element in the linked list.
        current_list: node_class.Node = first_half
        first_half = node_class.Node(node.data)
        first_half.next_node = current_list
        node = node.next_node

    while node.next_node is not None:
        # Compare the first half of the list with the second half.
        if node.data != first_half.data:
            return False

        first_half = first_half.next_node
        node = node.next_node

    if node.data != first_half.data:
        return False

    return True