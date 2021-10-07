# Inserindo nós em uma lista ligada

class Node:
    
    def __init__(self, _data):
        self.data = _data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    #Método para inserção de novos nós na frente (head)
    def push(self, _new_data):
        new_node = Node(_new_data)  # Criar novo nó (inserção direta dos dados para otimização)
        new_node.next = self.head   # Apontar o próximo do novo nó
        self.head = new_node        # Alocar o novo nó como head da lista
        
        return new_node
        
    
    # Método de inserção de um novo nó após um nó definido na lista
    def insert(self, _prev_node, _new_data):
        if _prev_node is None or _prev_node.next is None:   # Confirmar a existência do nó
            print("Nó deve pertencer à lista!")
            return
        
        new_node = Node(_new_data)                          # Criar novo nó (inserção direta dos dados para otimização)
        new_node.next = _prev_node.next                     # Apontar próximo do novo nó como o próximo do anterior
        _prev_node.next = new_node                          # Apontar o próximo do nó anterior como o novo
        
        return new_node    
    
    
    def insert_after_data(self, _prev_data, _new_data):
        new_node = Node(_new_data)                      # Criar novo nó (inserção direta dos dados para otimização)
        
        current = self.head                             # Criar nó auxiliar
        
        while current.data != _prev_data:               # Verificar se os dados no nó atual coincidem com os procurados
            current = current.next                      # Passar pro próximo nó
        
        if current is None or current.next is None:     # Identificar se o nó atual é o último
            print("Nó deve pertencer à lista")
            return
        
        new_node.next = current.next                    # Apontar o próximo do novo nó
        current.next = new_node                         # Apontar o próximo do nó atual
        
    
    # Método para inserir nós no final da lista
    def append(self, _new_data):
        new_node = Node(_new_data)  # Criar novo nó (inserção direta dos dados para otimização)
        
        if self.head is None:       # Descobrir se o head é vazio (e inserir o nó em caso positivo)
            self.head = new_node
            return
        
        last = self.head            # Definir o head como último nó
        
        while(last.next):           # Procurar pelo próximo vazio
            last = last.next
        
        last.next = new_node        # Inserir no final da lista
    
    
    def print_list(self):
        temp = self.head
        list_data = ""
        
        while(temp):
            list_data += str(temp.data) + " "
            temp = temp.next
        
        print(list_data)


l_list = LinkedList()
node_4 = l_list.push(4)
node_3 = l_list.push(3)
node_2 = l_list.push(2)
l_list.print_list()
print(l_list.head.next.data)

l_list.insert(node_3, 1)
node_1 = l_list.print_list()

l_list.insert(node_4, 1)
node_1 = l_list.print_list()

l_list.insert_after_data(1, 5)
l_list.print_list()

l_list.insert_after_data(4, 1)
l_list.print_list()