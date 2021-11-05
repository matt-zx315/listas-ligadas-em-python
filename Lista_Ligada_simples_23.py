# Somando e apagando os extremos de uma lista ligada
# REGRAS:
# 1- O número de nós deve ser par
# 2- Os valores somados devem ser os extremos da lista (primeiro e último)
# 3- Após a soma, os nós devem ser apagados
# 4- Processo se repete até a lista estar vazia
# 5- Retornar a maior soma
class Node:
    
    
    def __init__(self, _data):
        self.data = _data
        self.next = None


class Linked_List:
    
    
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
            list_data += str(temp.data) + " -> "
            temp = temp.next
        
        print(list_data)
    
    
    def get_length(self):
        length = 0
        pointer = self.head
        
        while pointer:
            length += 1
            pointer = pointer.next
        
        return length
    
    
    def sum_first_last(self):
        # sums = []
        highest_sum = 0
        current_sum = 0
        
        if self.get_length() % 2 != 0:
            return 0
        
        while self.head:
            last = self.head
            print(f'Primeiro nó: {self.head}\nDados: {self.head.data}')
            
            while last.next.next:
                last = last.next
            
            print(f'Último nó: {last.next}\nDados: {last.next.data}')
            # sums.append(self.head.data + last.next.data)
            current_sum = self.head.data + last.next.data
            
            if current_sum > highest_sum:
                highest_sum = current_sum
            
            print(f'{self.head.data} + {last.next.data} = {self.head.data + last.next.data}')
            last.next = None
            self.head = self.head.next
            self.print_list()
        
        # print(sums)
        return highest_sum


list1 = Linked_List()
list1.append(65)
list1.append(71)
list1.append(26)
list1.append(84)
list1.append(12)
list1.append(90)
list1.append(36)
list1.print_list()
print(list1.get_length())

list1.append(72)
list1.append(64)
list1.append(17)
list1.append(89)
list1.append(35)
list1.append(96)
list1.append(51)
list1.print_list()
print(list1.get_length())

print(list1.sum_first_last())
