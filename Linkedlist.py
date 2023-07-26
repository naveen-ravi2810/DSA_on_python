class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
            return
        else:
            node = self.head
            while(node.next!=None):
                node = node.next
            node.next = Node(data)
            return

    def show(self):
        node = self.head
        while node != None:
            print(node.data, end="->")
            node = node.next
        print("\n")

    def kthelementfromlast(self, k):
        length = 0
        node = self.head

        while(node.next!=None):
            length += 1
            node = node.next
        if (length+1 >= k):
            pos = length-k
            i = 0
            node = self.head
            while(i<=pos):
                node = node.next
                i += 1
            print(node.data)
        else:
            print("The Linked List Length is short")

ll = LL()

while 1:
    print("1 -> Add Element\n2 -> Show Element\n3 -> kthelementfromlast\n0 -> Exit")
    choice = int(input("Enter Your Choice : "))
    if (choice == 1):
        data = int(input("Enter the data : "))
        ll.insert(data)
    elif (choice == 2):
        ll.show()
    elif (choice == 3):
        k = int(input("Enter the element from last : "))
        ll.kthelementfromlast(k)
    elif (choice == 0):
        print("Thanks for having us")
        break
    else:
        print("Enter the correct choice")
        continue
# ll.insert(1)
# ll.insert(2)
# ll.insert(3)
# ll.show()

