# Removendo valores duplicados de uma lista
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
    
    
    def remove_duplicates(self):
        current = self.head
        previous = None         # Aponta para o nó anterior
        
        dupes = set()
        
        while current:
            if current.data not in dupes:
                dupes.add(current.data)
                previous = current
            else:
                previous.next = current.next
            
            current = current.next


list1 = LinkedList()
list1.append(10)
list1.append(11)
list1.append(11)
list1.append(12)
list1.append(12)
list1.append(13)
list1.append(14)
list1.append(15)
list1.append(15)
list1.append(15)
list1.append(15)
list1.append(16)
list1.append(17)
list1.print_list()

list1.remove_duplicates()
list1.print_list()

list2 = LinkedList()
list2.append(20)
list2.append(40)
list2.append(15)
list2.append(15)
list2.append(16)
list2.append(8)
list2.append(8)
list2.append(8)
list2.append(16)
list2.append(7)
list2.append(5)
list2.append(6)
list2.append(2)
list2.append(2)
list2.append(40)
list2.append(20)
list2.append(35)
list2.append(76)
list2.append(59)
list2.print_list()

list2.remove_duplicates()
list2.print_list()
