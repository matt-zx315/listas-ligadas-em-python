# Encontrando loops em uma lista ligada
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None
        self.flag = False


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
    
    # Método 1: Usando hash
    def find_loop_hash(self):
        pointer = self.head
        hash_table = set()
        
        while(pointer):
            if pointer in hash_table:
                return f"Loop encontrado!\n\nNó: {pointer}\nValor: {pointer.data}\nPróximo: {pointer.next}\nValor: {pointer.next.data}"
            
            hash_table.add(pointer)
            pointer = pointer.next
        
        return "Nenhum loop encontrado."
    
    
    # Método 2: Visitando e marcando nós
    def find_loop_flag(self):
        pointer = self.head
        
        while (pointer):
            if (pointer.flag):
                return f"Loop encontrado!\n\nNó: {pointer}\nValor: {pointer.data}\nPróximo: {pointer.next}\nValor: {pointer.next.data}"
            
            pointer.flag = True
            pointer = pointer.next
        
        return "Nenhum loop encontrado."
    
    
    # Método 3: Ciclo de Floyd
    def find_loop_floyd(self):
        slow = self.head
        fast = self.head
        
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if(slow == fast):
                return f"Loop encontrado!\n\nNó: {slow}\nValor: {slow.data}\nPróximo: {fast.next}\nValor: {fast.next.data}"
        
        return "Nenhum loop encontrado."
    
    
    # Método 4: Marcando nós visitados com um nó temporário (destroi a lista por completo e fode o rolê)
    def find_loop_temp(self):
        aux = self.head
        temp = Node(0)
        
        while(aux):
            if aux.next == temp:
                return f"Loop encontrado!\n\nNó: {aux}\nValor: {aux.data}"
            
            next_node = aux.next
            aux.next = temp
            aux = next_node
        
        return "Nenhum loop encontrado."
    
    
    # Método 5: Medição de distância de dois ponteiros
    def get_distance(self, _first, _last):
        distance = 0
        
        while(_first != _last):
            _first = _first.next
            distance += 1
        
        return distance
    
    
    def find_loop_distance(self):
        first = self.head
        last = self.head
        this_distance = 0
        previous_distance = 0
        
        while(last):
            this_distance = self.get_distance(first, last)
            
            if this_distance < previous_distance:
                return f"Loop encontrado!\n\nNó: {last}\nValor: {last.data}\nPróximo: {last.next}\nValor: {last.next.data}"
            
            previous_distance = this_distance
            last = last.next
        
        return "Nenhum loop encontrado."
            


l_list = LinkedList()
l_list.append(65)
l_list.append(71)
l_list.append(26)
l_list.append(84)
l_list.append(12)
l_list.append(90)
l_list.append(36)
l_list.print_list()

# node1 = l_list.get_node_data(71)
# node2 = l_list.get_node_data(90)

# print(l_list.get_distance(node1, node2))

# print(l_list.find_loop_hash())
# print(l_list.find_loop_flag())
# print(l_list.find_loop_floyd())
# print(l_list.find_loop_temp())
print(l_list.find_loop_distance())

l_list.get_node_data(36).next = l_list.head
# print(l_list.find_loop_hash())
# print(l_list.find_loop_flag())
# print(l_list.find_loop_floyd())
# print(l_list.find_loop_temp())
print(l_list.find_loop_distance())
