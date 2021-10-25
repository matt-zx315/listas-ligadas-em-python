# Encontrando o ponto de intersecção comum de duas listas
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None
    
    
    def __repr__(self):
        return f'Objeto tipo: {self.__class__.__module__}\nNome: {self.__class__.__name__}\n' \
        f'Endereço: {hex(id(self))}\nDados: {self.data}\n'


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
    
    
    def get_node_data(self, _data):
        count = 0
        node = self.head
    
        if self.head is None:
            return
        
        while node.data != _data:
           node = node.next
           count += 1
        
        return node
    
    
    def find_intersection_node(self, _list):
        list_pointer = self.head
        
        nodes = set()
        
        while list_pointer:
            nodes.add(list_pointer)
            list_pointer = list_pointer.next
        
        list_pointer = _list.head
        
        while list_pointer:
            if list_pointer in nodes:
                return list_pointer
            
            list_pointer = list_pointer.next


list1 = LinkedList()
list1.append(3)
list1.append(6)
list1.append(9)
list1.append(15)
list1.append(30)
list1.print_list()

list2 = LinkedList()
list2.append(10)
list2.get_node_data(10).next = list1.get_node_data(9)
list2.print_list()

print(list1.find_intersection_node(list2))
