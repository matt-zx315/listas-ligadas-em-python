# Apagando nó de lista ligada passando sua posição
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


    def delete_node(self, _index):
        temp = self.head
        
        if self.head is None:
            print("Lista vazia. Tão vazia quanto a sua alma!")
            return
        elif _index == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(_index - 1):
            temp = temp.next
        
        if temp is None or temp.next is None:
            print("Nó inexistente na lista!")
            return
        
        new_next = temp.next.next
        temp.next = None
        temp.next = new_next


l_list = LinkedList()
l_list.delete_node(5)

l_list.push('c')
l_list.push('f')
l_list.push('b')
l_list.push('a')

l_list.print_list()

l_list.delete_node(0)
l_list.print_list()

l_list.delete_node(1)
l_list.print_list()

l_list.delete_node(3)
l_list.print_list()