class Node:
    nextNode: "Node" = None
    data: int

    def __init__(self: "Node", data: int):
        self.data = data

    def append_to_tail(self: "Node", data: int):
        endNode: "Node" = Node(data)
        currentNode: "Node" = self
        while (currentNode.nextNode != None):
            currentNode = currentNode.nextNode
        currentNode.nextNode = endNode