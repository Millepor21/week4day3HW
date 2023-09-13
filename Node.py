class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return f'<Node: {self.value}>'

# node = Node('monday')

# node2 = Node('Tuesday')

# node.right = node2

# node3 = Node('Wednesday')

# node2.right = node3

# node4 = Node('Thursday')

# node5 = Node('Friday')

# node6 = Node('Saturday')

# node7 = Node('Sunday')

# node3.right = node4

# node4.right = node5

# node5.right = node6

# node6.right = node7

# node7.right = node

# print(node, node.right, node.right.right, node.right.right.right, node.right.right.right.right, node.right.right.right.right.right, node.right.right.right.right.right.right)