# Trocando valores de lugar sem mover nós
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
        count = 0
        node = self.head
    
        if self.head is None:
            return
        
        while node.data != _data:
           node = node.next
           count += 1
        
        return node
    
    
    def swap_values(self, _val1, _val2):
        node_1 = self.get_node_data(_val1)
        node_2 = self.get_node_data(_val2)
        
        if node_1 and node_2:
            aux = node_1.data
            node_1.data = node_2.data
            node_2.data = aux
            return
        
        print("Valor(es) não encontrado(s)!")
    
    
    # Atravessando a lista uma única vez
    def swap_data(self, _data1, _data2):
        node_1 = None
        node_2 = None
        
        ref = self.head
        
        while ref:
            if (ref.data == _data1 or ref.data == _data2) and node_1 is None:
                node_1 = ref
            elif (ref.data == _data1 or ref.data == _data2) and node_2 is None:
                node_2 = ref
            
            ref = ref.next
            
        if node_1 and node_2:
            aux = node_1.data
            node_1.data = node_2.data
            node_2.data = aux
            return
        
        print("Valor(es) não encontrado(s)!")


list1 = LinkedList()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()
print(list1.get_node_data(26))
print(list1.get_node_data(84))

# list1.swap_values(26, 84)
list1.swap_data(26, 84)
list1.print_list()
print(list1.get_node_data(26))
print(list1.get_node_data(84))

# list1.swap_values(65, 71)
list1.swap_data(65, 71)
list1.print_list()

# list1.swap_values(90, 36)
list1.swap_data(90, 36)
list1.print_list()

# list1.swap_values(71, 90)
list1.swap_data(71, 90)
list1.print_list()

list1.swap_data(24, 69)
list1.print_list()
