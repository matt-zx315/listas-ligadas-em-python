# Tamanho de uma lista
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    def push(self, _new_data):
        new_node = Node(_new_data)
        new_node.next = self.head
        self.head = new_node
    

    def print_list(self):
        temp = self.head
        list_data = ""
        
        while(temp):
            list_data += str(temp.data) + " "
            temp = temp.next
        
        print(list_data)
    
    
    # método iterativo
    def return_length(self):
        count = 0
        node = self.head
        
        while(node):
            count += 1
            node = node.next
        
        return count
    
    
    # método recursivo
    def get_length_recursive(self, _node):
        if not _node:
            return 0
        return 1 + self.get_length_recursive(_node.next)
    
    
    def get_length(self):
        return self.get_length_recursive(self.head)


l_list = LinkedList()
print(l_list.get_length())

node_4 = l_list.push(4)
node_3 = l_list.push(3)
node_2 = l_list.push(2)
l_list.print_list()

print(l_list.return_length())
print(l_list.get_length())