class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data 
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, data):
        if (self.head != None):
            node = self.head
            while(node.next != None):
                node = node.next
            new_node = Node(data)
            node.next = new_node
            new_node.prev = node
            new_node.next = None
        else:
            new_node = Node(data)
            self.head = new_node
            new_node.prev = None
            new_node.next = None
            
    def show(self):
        if(self.head == None):
            print("List is Empty")
        else:
            node = self.head
            while(node.next != None):
                print(node.data, end="->")
                node = node.next
            print(node.data)
        print("\n")    

    def kthelementfromlast(self,k):
        node = self.head
        while(node.next != None):
            node = node.next
        i = 0 
        while i<k-1 and node.prev!=None:
            node = node.prev
            i += 1
        print(node.data)
        

dll = DoublyLinkedList()
while 1:
    print("1 -> Add Element\n2 -> Show Element\n3 -> kthelementfromlast\n0 -> Exit")
    choice = int(input("Enter Your Choice : "))
    if (choice == 1):
        data = int(input("Enter the data : "))
        dll.insert(data)
    elif (choice == 2):
        dll.show()
    elif (choice == 3):
        k = int(input("Enter the element from last : "))
        dll.kthelementfromlast(k)
    elif (choice == 0):
        print("Thanks for having us")
        break
    else:
        print("Enter the correct choice")
        continue