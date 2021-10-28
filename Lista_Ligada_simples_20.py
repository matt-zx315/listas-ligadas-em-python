# Separando valores pares e ímpares
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
    
    
    def segregate_odd_even(self):
        odd_start, odd_end = None, None
        even_start, even_end = None, None
        pointer = self.head
        
        if pointer is None or pointer.next is None:
            return
        
        while pointer:
            data = pointer.data
            if(data % 2 == 0):
                if even_start is None:
                    even_start = pointer
                    even_end = even_start
                else:
                    even_end.next = pointer
                    even_end = even_end.next
            else:
                if odd_start is None:
                    odd_start = pointer
                    odd_end = odd_start
                else:
                    odd_end.next = pointer
                    odd_end = odd_end.next
            
            pointer = pointer.next
        
        self.head = even_start
        even_end.next = odd_start
        odd_end.next = None


list1 = LinkedList()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

list1.segregate_odd_even()
list1.print_list()
