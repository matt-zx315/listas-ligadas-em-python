# Encontrando o enésimo nó a partir do final da lista (qual a utilidade disso???)
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


    def get_length(self):
        node = self.head
        len = 0
        
        if node is None:
            return 0
        
        while(node):
            node = node.next
            len += 1
        
        return len
    
    
    # Método com um ponteiro
    def reverse_search(self, _pos):
        pointer = self.head
        count = 0
        
        while(pointer):
            if count == (self.get_length() - _pos - 1):
                return pointer.data
            
            #print(count)
            pointer = pointer.next
            count += 1
        
        return "Tem saporra aqui não!"
    
    
    # Método com 2 ponteiros
    def reverse_search_2pointer(self, _pos):
        main_pointer = self.head
        aux_pointer = self.head
        
        for i in range(_pos + 1):
            if aux_pointer.next is None:
                return "Posição inexistente"
            
            aux_pointer = aux_pointer.next
        
        while(aux_pointer):
            aux_pointer = aux_pointer.next
            main_pointer = main_pointer.next
            
        return main_pointer.data


l_list = LinkedList()
l_list.push(65)
l_list.push(71)
l_list.push(26)
l_list.push(84)
l_list.push(12)
l_list.push(90)
l_list.print_list()
print(l_list.get_length())

print(l_list.reverse_search(2))
print(l_list.reverse_search_2pointer(2))

print(l_list.reverse_search(9))
print(l_list.reverse_search_2pointer(9))
