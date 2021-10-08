# Desbrindo o tamanho do loop na lista
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
    
    
    def get_length(self):
        node = self.head
        len = 0
        
        if node is None:
            return 0
        
        while(node):
            node = node.next
            len += 1
        
        return len
        
    
    def create_loop(self, _start_data,_end_data):
        self.get_node_data(_start_data).next = self.get_node_data(_end_data)
        
    
    
    def find_loop_end(self):
        hash_table = set()
        pointer = self.head
        
        while pointer.next not in hash_table:
            hash_table.add(pointer)
            pointer = pointer.next
        
        return pointer
    
    
    def find_loop_floyd(self):
        slow = self.head
        fast = self.head
        
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if(slow == fast):
                return (slow, fast)
        
        return None
    
    
    def break_loop(self):
        self.find_loop_end().next = None
    
    
    def get_loop_length(self):
        loop_found = self.find_loop_floyd()
        
        if loop_found is None:
            return 0
        
        slow = loop_found[0].next
        fast = loop_found[1]
        count = 1
        
        while (slow is not fast):
            count += 1
            slow = slow.next
        
        return count


l_list = LinkedList()
l_list.append(65)
l_list.append(71)
l_list.append(26)
l_list.append(84)
l_list.append(12)
l_list.append(90)
l_list.append(36)
l_list.print_list()

print(l_list.get_length())
print(l_list.get_loop_length())

l_list.create_loop(36, 65)
print(l_list.get_loop_length())

l_list.create_loop(36, 26)
print(l_list.get_loop_length())

l_list.break_loop()
print(l_list.get_loop_length())
