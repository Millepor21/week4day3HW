from BST import BinarySearchTree

from Node import Node

class LinkedList:

    def __init__(self, head_value=None,unsorted_linked_list=[]):
        self.head = Node(head_value)
        self.unsorted_Linked_List = unsorted_linked_list
        self.unsorted_Linked_List.append(self.head.value)
    def __repr__(self):
        return f'<LinkedList: {" -> ".join(str(node.value) for node in self if str(node.value) != "None")}>'
    
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
        self.unsorted_Linked_List.append(current_node.right.value)

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

    def sort_Linked_List(self):
        root_term = self.unsorted_Linked_List[0]
        unsorted_list = self.unsorted_Linked_List
        bst = BinarySearchTree(root_term)
        for value in unsorted_list:
            bst.add_node(value)
        sorted_list = bst.append_sorted()
        linkedlist_hw_sorted = LinkedList()
        for num in sorted_list:
            linkedlist_hw_sorted.append_node(num)
        print(linkedlist_hw_sorted)
             
        
        

linkedlist_hw = LinkedList(30)

linkedlist_hw.append_node(20)
linkedlist_hw.append_node(10)
linkedlist_hw.append_node(40)
linkedlist_hw.append_node(50)
linkedlist_hw.append_node(60)
linkedlist_hw.append_node(15)
linkedlist_hw.append_node(105)
linkedlist_hw.append_node(115)
linkedlist_hw.append_node(88)
linkedlist_hw.append_node(99)
linkedlist_hw.append_node(55)

linkedlist_hw.sort_Linked_List()