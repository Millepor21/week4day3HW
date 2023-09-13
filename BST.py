from Node import Node

class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)
        self.sorted_list = []

    def __repr__(self):
        return f'<BST: {self.root}'
    
    def add_node(self, value, current_node=None):
        if not current_node:
            current_node = self.root
        if value > current_node.value:
            if current_node.right:
                self.add_node(value, current_node.right)
            else:
                current_node.right = Node(value)
        elif value < current_node.value:
            if current_node.left:
                self.add_node(value, current_node.left)
            else:
                current_node.left = Node(value)

    def search(self, value, current_node=None):
        if not current_node:
            current_node = self.root
        if value > current_node.value:
            if current_node.right:
                return self.search(value, current_node.right)
        elif value < current_node.value:
            if current_node.left:
                return self.search(value, current_node.left)
        elif value == current_node.value:
            return current_node
        print(f'Node: {value} not found')
        return False

    def get_min(self):
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node

    def get_max(self):
        current_node = self.root
        while current_node.right:
            current_node = current_node.right
        return current_node
        
    def get_max_rec(self, current_node=None):
        if not current_node:
            current_node = self.root
        if current_node.right:
            current_node = current_node.right
            return self.get_max_rec(current_node)
        return current_node

    def print_sorted(self, current_node=None):
        if not current_node:
            current_node = self.root
        if current_node.left:
            self.print_sorted(current_node.left)
        print(current_node.value)
        if current_node.right:
            self.print_sorted(current_node.right)

    def append_sorted(self, current_node=None):
        if not current_node:
            current_node = self.root
        if current_node.left:
            self.append_sorted(current_node.left)
        self.sorted_list.append(current_node.value)
        if current_node.right:
            self.append_sorted(current_node.right)
        return self.sorted_list

    def print_sorted_reverse(self, current_node=None):
        if not current_node:
            current_node = self.root
        if current_node.right:
            self.print_sorted_reverse(current_node.right)
        print(current_node.value)
        if current_node.left:
            self.print_sorted_reverse(current_node.left)

# bst = BinarySearchTree(100)
# bst.add_node(125)
# bst.add_node(130)
# bst.add_node(115)
# bst.add_node(50)
# bst.add_node(75)
# bst.add_node(25)
# bst.add_node(110)
# bst.add_node(120)

# print(bst.root.right.right)
# print(bst.root.right.left)
# print(bst.root.left.right)
# bst.search(135)

# print(bst.get_min())
# print(bst.get_max())
# print(bst.get_max_rec())
# bst.print_sorted()
# bst.print_sorted_reverse()