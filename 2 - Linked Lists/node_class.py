class Node:
    next_node: "Node" = None
    data: int

    def __init__(self: "Node", data: int):
        self.data = data

    def append_to_tail(self: "Node", data: int):
        end_node: "Node" = Node(data)
        current_node: "Node" = self
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = end_node
