class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head()
        length = 0
        while current.next != None:
            length +=1;
            current = current.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        return elems;

    def get(self, index):
        current = self.head
        count = 0
        while current.next != None:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return 'Error: Index out of range'

    def remove(self,data):
        current = self.head
        previous_node = None
        while current.data != data:
            previous_node = current
            current = current.next
        previous_node.next = current.next
        if not data:
            return 'Error invalid dara'

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(5)
my_list.append('HEllo')
print(my_list.display())
print(my_list.get(2))
print(my_list.display())
