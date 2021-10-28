# Criando uma lista ligada ordenada
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    
    def insert_ordered(self, _new_data):
        new_node = Node(_new_data)
        aux = self.head
        
        # Se o head da lista for vazio...
        if self.head is None:
        
            # ...o novo nó será o head.
            self.head = new_node
            
        # Caso a lista só tenha um nó:
        elif self.head.next is None:
        
            # 1 - ele pode ter um valor menor do que o do head...
            if new_node.data <= self.head.data:
            
                # ...então ele deve ser o novo head.
                new_node.next = aux
                self.head = new_node
                
            # 2 - mas ele pode não ser...
            else:
            
                # ...caso em que ele será o próximo do head
                self.head.next = new_node
                
        # E no caso da lista ter dois ou mais nós:
        else:
        
            # 1 - esse novo nó pode ter valor menor que o head...
            if new_node.data <= self.head.data:
            
                # ...caso em que ele será o novo head.
                new_node.next = aux
                self.head = new_node
                
            # 2 - ou não...
            else:
            
                # ...então criamos um ponteiro pro head e pro próximo do head...
                previous, current = self.head, self.head.next
                
                # ...e corremos a lista com eles:
                while current:
                
                    # 1 - Vemos se o valor do nó é menor do que o do nó atual...
                    if new_node.data <= current.data:
                    
                        # ...e em caso positivo, inserimos o novo nó entre o anterior e o atual.
                        print(True)
                        previous.next = new_node
                        new_node.next = current
                        return
                    
                    # 2 - Caso não seja, continuamos a avançar na lista
                    else:
                        previous = current
                        current = current.next
                    
                # Se em nenhum momento o novo nó se encaixar, isso quer dizer que ele é o último da lista.
                previous.next = new_node
    

    def print_list(self):
        temp = self.head
        list_data = ""
        
        while(temp):
            list_data += str(temp.data) + " "
            temp = temp.next
        
        print(list_data)

list1 = LinkedList()
list1.insert_ordered(65)
list1.insert_ordered(71)
list1.insert_ordered(26)
list1.insert_ordered(84)
list1.insert_ordered(12)
list1.insert_ordered(90)
list1.insert_ordered(36)
list1.print_list()
