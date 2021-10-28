# Ordenar valores de uma lista ligada
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
    
    
    # Método 1 - trollando com vetores
    def set_values(self, _values):
        aux = self.head
        
        while aux:
            aux.data = _values.pop()
            aux = aux.next
    
    
    def sort(self):
        aux = self.head
        data = []
        
        while aux:
            data.append(aux.data)
            aux = aux.next
        
        data = sorted(data, reverse=True)
        
        self.set_values(data)
    
    
    # Método 2 - cirando e retornando uma nova lista ordenada
    def insert_ordered(self, _new_data):
        new_node = Node(_new_data)
        aux = self.head
        
        
        if self.head is None:
            self.head = new_node
        elif self.head.next is None:
            if new_node.data <= self.head.data:
                new_node.next = aux
                self.head = new_node
            else:
                self.head.next = new_node
        else:
            if new_node.data <= self.head.data:
                new_node.next = aux
                self.head = new_node
            else:
                previous, current = self.head, self.head.next
                while current:
                    if new_node.data <= current.data:
                        previous.next = new_node
                        new_node.next = current
                        return
                    else:
                        previous = current
                        current = current.next
                previous.next = new_node
    
    
    def sort_list(self):
        ordered_list = LinkedList()
        aux = self.head
        
        while aux:
            ordered_list.insert_ordered(aux.data)
            aux = aux.next
        
        return ordered_list


list1 = LinkedList()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

# list1.sort()
# list1.print_list()

list1.sort_list().print_list()
list1 = list1.sort_list()
list1.print_list()
