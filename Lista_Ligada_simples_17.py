# Ponto de intersecção entre duas listas
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
    
    
    def find_intersection_hash(self, _list1, _list2):
        intersection = LinkedList()
        
        pointer_1 = _list1.head
        pointer_2 = _list2.head
        
        dupes = set()
        
        while pointer_1:
            dupes.add(pointer_1.data)
            pointer_1 = pointer_1.next
        
        while pointer_2:
            if pointer_2.data in dupes:
                intersection.append(pointer_2.data)
            
            pointer_2 = pointer_2.next
        
        return intersection


list1 = LinkedList()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

list2 = LinkedList()
list2.append(21)
list2.append(36)
list2.append(44)
list2.append(9)
list2.append(12)
list2.append(65)
list2.append(10)
list2.print_list()

intersection = list1.find_intersection_hash(list1, list2)
intersection.print_list()