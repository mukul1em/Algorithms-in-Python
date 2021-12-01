
class node:
    #by default data is set to None
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node() #only used as a place holder to allow us to point at the first element in the linked list
    
    #function to append data point at the end of the current list
    #where next is pointing to None
    def append(self, data):
        #node to appended
        new_node  = node(data)
        cur  = self.head
        while cur.next != None:
            cur = cur.next
        #next value is equal to none then set the new node at the end 
        cur.next = new_node
    #function to find the length of the linked list
    #counting number of nodes till it points to none
    def length(self):
        cur  = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next #traversing through the next node
        
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
            
        print(elems)
    #retrieving element at the certain index in linked list
    def get(self, index):
        if index >= self.length():
            print("ERROR: get() index out of range")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1
    
    #erasing element at the certain index in the list
    def erase(self, index):
        if index >= self.length():
            print("ERROR: get() index out of range")
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return 
            cur_index+=1
        
            

            



my_list = linked_list() #creating instance of linked list
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print(my_list.erase(3))
my_list.display()



    
    






