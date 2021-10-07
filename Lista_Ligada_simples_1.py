#Classe Nó
class Node:
    
    #Construtor do nó
    def __init__(self, _data):
        self.data = _data  #Pode ser absolutamente qualquer coisa
        self.next = None   #O próximo nó da lista


#Classe da lista ligada (simples)
class LinkedList:
    
    #Construtor da lista
    def __init__(self):
        self.head = None  #O primeiro elemento da lista
    
    
    #Imprimindo elementos da lista
    def print_list(self):
        temp = self.head  #Nó temporário que vai passar capturar os valores dos dados armazenados
        list_data = ""
        
        while(temp):
            list_data += str(temp.data) + " "
            temp = temp.next
        
        print(list_data)


if __name__ == '__main__':

    l_list = LinkedList()
    l_list.head = Node(1)

    print(l_list.head.data)
    
    second = Node(2)
    third = Node(3)
    
    l_list.head.next = second
    second.next = third
    
    print(l_list.head.next.next.data)
    
    l_list.print_list()