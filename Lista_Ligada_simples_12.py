# Descobrindo se a lista é um palíndromo
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    def append(self, _new_data):
        new_node = Node(_new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        
        while(last.next):
            last = last.next
        
        last.next = new_node
    
    
    def get_node_data(self, _data):
        count = 0
        node = self.head
    
        if self.head is None:
            return
        
        while node.data != _data:
           node = node.next
           count += 1
        
        return node
    

    def print_list(self):
        if self.head is None:
            print("Vazio... Igualzinho tua cabeça!!!")
            return
        
        temp = self.head
        list_data = ""
        
        while(temp):
            list_data += str(temp.data) + " "
            temp = temp.next
        
        print(list_data)
    
    
    def create_stack(self):
        temp = self.head
        data_stack = []
        
        while temp is not None:
            data_stack.append(temp.data)
            temp = temp.next
        
        return data_stack
    
    
    def is_palyndrome_stack(self):
        temp = self.head
        data_stack = self.create_stack()
        
        while temp is not None:
            if temp.data != data_stack.pop():
                return False
            
            return True


link_list1 = LinkedList()
link_list1.append('r')
link_list1.append('a')
link_list1.append('d')
link_list1.append('a')
link_list1.append('r')
link_list1.print_list()
print(link_list1.is_palyndrome_stack())

link_list2 = LinkedList()
link_list2.append('e')
link_list2.append('g')
link_list2.append('g')
link_list2.print_list()
print(link_list2.is_palyndrome_stack())
