# Colocando o último nó da lista na frente
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
    
    
    def find_last(self):
        node = self.head
        
        while node.next.next:   # É necessário olhar dois nós à frente porque o nó atual será o penúltimo
            node = node.next
        
        return node.next, node
    
    
    def last_to_head(self):
        last, second_last = self.find_last()
        
        second_last.next = None
        last.next = self.head
        self.head = last


list1 = LinkedList()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

list1.last_to_head()
list1.print_list()
