# Encontrando o valor do enésimo nó na lista
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
    
    
    # Método iterativo
    def get_position(self, _position):
        current = self.head
        count = 0
        
        while current:
            if count == _position:
                return current.data
            
            current = current.next
            count += 1
        
        return f"Não existe a posição {_position} na lista."
    
    
    # Método recursivo
    def get_nth(self, _position):
        return self.get_nth_recursive(self.head, _position)
    
    
    def get_nth_recursive(self, _head, _position):
        count = 0
        
        if(_head):
            if count == _position:
                return _head.data
            
            count += 1
            self.get_nth_recursive(_head.next, _position)
        
        return "Saporra non ecxiste!"


l_list = LinkedList()
l_list.push(65)
l_list.push(71)
l_list.push(26)
l_list.push(84)
l_list.push(12)
l_list.push(90)
l_list.print_list()

pos = 0
print(f"O valor na posição {pos} é {l_list.get_position(pos)}")
print(l_list.get_nth(pos))

pos = 10
print(l_list.get_position(pos))
print(l_list.get_nth(pos))