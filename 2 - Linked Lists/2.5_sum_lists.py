# You have two numbers represented by a linked list, where each node contains a single digit. The digits
# are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that
# adds the two numbers and returns the sum as a linked list.

import node_class


def sum_lists(num1: node_class.Node, num2: node_class.Node) -> node_class.Node:
    output: node_class.Node = node_class.Node(0)
    output_head: node_class.Node = output
    remainder: int = 0

    while num1 is not None or num2 is not None:
        sum: int = remainder
        if num1 is not None:
            sum += num1.data
        if num2 is not None:
            sum += num2.data

        if sum >= 10:
            remainder = 1
            output.next_node = node_class.Node(sum - 10)
        else:
            remainder = 0
            output.next_node = node_class.Node(sum)
        
        output = output.next_node
        num1 = num1.next_node
        num2 = num2.next_node

    if remainder > 0:
        output.next_node = node_class.Node(remainder)

    return output_head.next_node