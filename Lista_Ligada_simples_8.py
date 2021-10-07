# Imprimindo o meio da lista
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    def push(self, _new_data):
        new_node = Node(_new_data)
        new_node.next = self.head
        self.head = new_node
    

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


    def get_length(self):
        node = self.head
        len = 0
        
        if node is None:
            return 0
        
        while(node):
            node = node.next
            len += 1
        
        return len
    
    
    # Método 1: Encontrar o tamanho da lista e dividir por 2
    def print_middle_by_length(self):
        if self.head is None:
            print("Lista vazia")
            return
        
        aux = self.head
        
        for i in range(int(self.get_length()/2)):
            aux = aux.next
        
        print(aux.data)
    
    
    # Método 2: Encontrar o tamanho da lista com dois ponteiros
    def print_middle_with_2pointers(self):
        if self.head is None:
            print("Lista vazia")
            return
        
        main = self.head
        aux = self.head
        
        while(aux) and (aux.next):
            aux = aux.next.next
            main = main.next
        
        print(main.data)


l_list = LinkedList()
l_list.push(65)
l_list.push(71)
l_list.push(26)
l_list.push(84)
l_list.push(12)
l_list.push(90)
l_list.push(36)
l_list.print_list()
print(l_list.get_length())

l_list.print_middle_by_length()
l_list.print_middle_with_2pointers()
