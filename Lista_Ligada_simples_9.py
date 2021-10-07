# Contando o número de vezes que um valor se repete na lista
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


    def get_length(self):
        node = self.head
        len = 0
        
        if node is None:
            return 0
        
        while(node):
            node = node.next
            len += 1
        
        return len
    
    
    # Método iterativo
    def count_data(self, _data):
        aux = self.head
        count = 0
        
        if self.head is None:
            print("Lista vazia... Vazia igual a sua alma...")
            return
        
        while(aux):
            if(aux.data == _data):
                count += 1
            
            aux = aux.next
        
        print(f"O valor {_data} aparece {count} vez(es).")
    
    
    # Método recursivo
    def count_data_recursive(self, _head, _data, _freq = 0):        #  NUNCA ALTERAR O VALOR DE FREQ
        
        if _head is None:
            return _freq
        
        if _head.data == _data:
            _freq += 1
        
        return self.count_data_recursive(_head.next, _data, _freq)  #  Por quê return é necessário? Porque a função retorna um valor no final


l_list = LinkedList()

l_list.count_data(1)

l_list.append(2)
l_list.append(3)
l_list.append(3)
l_list.append(4)
l_list.append(2)
l_list.append(1)
l_list.append(3)
l_list.append(2)
l_list.print_list()

l_list.count_data(1)
l_list.count_data(2)
l_list.count_data(3)
l_list.count_data(4)

print(l_list.count_data_recursive(l_list.head, 3))
