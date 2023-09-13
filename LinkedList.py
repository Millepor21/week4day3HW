from Node import Node

class LinkedList:

    def __init__(self, head_value):
        self.head = Node(head_value)
    
    def __repr__(self):
        # output = f'<LinkedList: '
        # for node in self:
        #     output += f'{node.value} -> '
        # return output.rstrip(' -> ')
        return f'<LinkedList: {" -> ".join(node.value for node in self)}>'
    
    def __iter__(self):
        current_node = self.head
        while current_node.right:
            yield current_node
            current_node = current_node.right
        yield current_node
    
    def append_node(self, value):
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = Node(value)

    def insert(self, neighbor, value):
        for node in self:
            if node.value == neighbor:
                next_node = node.right
                node.right = Node(value)
                node.right.right = next_node
                return
        return print(f'{neighbor} not in LinkedList')
    
    def update_head(self, value):
        old_head = self.head
        self.head = Node(value)
        self.head.right = old_head
        # new_head = Node(value)
        # new_head.right = self.head
        # self.head = new_head

    def search(self, value):
        for node in self:
            if node.value == value:
                return node
        return False

    def get_tail(self):
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        return current_node
    
    def get_tail_dylan(self):
        for node in self:
            pass
        return node

    
    def remove(self,value):
        old_node = []
        for node in self:
            if node.value == value:
                last_node = old_node[-1]
                last_node.right = node.right
               
            else:
                old_node.append(node)


linkedlist = LinkedList('Monday')

linkedlist.append_node('Tuesday')
linkedlist.append_node('Wednesday')
linkedlist.append_node('Friday')
linkedlist.append_node('Saturday')

# print(linkedlist.search('Monday'))
# print(linkedlist.search('Friday'))

# # print(linkedlist.head.right)

linkedlist.insert('Wednesday','Thursday')
# linkedlist.insert('Saturday','Sunday')

linkedlist.update_head('Sunday')

print(linkedlist)
# linkedlist.remove('Monday')

# for node in linkedlist:
#     # print(node)
#     print(linkedlist.search(node.value))

# print(linkedlist.get_tail())
# print(linkedlist.get_tail_dylan())
