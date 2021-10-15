# Trocando nós de posição
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
    
    
    # Atravessando a lista duas vezes
    def get_node_data(self, _data):
        current = self.head
        previous = None
        
        while current and current.data != _data:
            previous = current
            current = current.next
        
        return current, previous
    
    
    def swap_positions(self, _val1, _val2):
        if _val1 == _val2:
            return
        
        current_1, previous_1 = self.get_node_data(_val1)
        current_2, previous_2 = self.get_node_data(_val2)
        
        if current_1 == None or current_2 == None:
            return
        
        if previous_1 != None:
            previous_1.next = current_2
            print(f"{previous_1.data} -> {previous_1.next.data}")
        else:
            self.head = current_2
            print(f"{self.head.data} -> {self.head.next.data}")
        
        if previous_2 != None:
            previous_2.next = current_1
            print(f"{previous_2.data} -> {previous_2.next.data}")
        else:
            self.head = current_1
            print(f"{self.head.data} -> {self.head.next.data}")
        
        temp = current_1.next
        current_1.next = current_2.next
        print(f"{current_1.data} -> {current_1.next.data}")
        current_2.next = temp
        if current_2.next:
            print(f"{current_2.data} -> {current_2.next.data}")
        else:
            print(f"{current_2.data} -> {None}")
        
        
list1 = LinkedList()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()

list1.swap_positions(26, 90)
list1.print_list()

list1.swap_positions(65, 84)
list1.print_list()

list1.swap_positions(36, 71)
list1.print_list()
