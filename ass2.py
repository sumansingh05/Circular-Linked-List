class Node:
    def __init__(self,data):
        self.item= data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def search(self,data):
        current = self.head
        while current:
            if current.item == data:
                return current
            current = current.next
        return None
    
    #adding a node at the starting of the circular linked list
    def addFirst(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.head = newNode

    #adding a node at the end of the circular linked list
    def addLast(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode

    #adding a new node inside  the circular linked list after a given node
    def addInside(self,current,data):
        if current == None:
            print("Node is not present in the List")        
        else:
            newNode = Node(data)
            if current == self.tail:
                self.addLast(data)
            else:                
                newNode.next = current.next
                current.next = newNode

    #deleting a node at the starting of circular Linked List
    def deleteAtFirst(self):
        if self.is_empty():
            print("List is empty!")
        elif self.head.next is self.head:
            self.head = None
            self.tail = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next    

    #deleting a node at the end of circular Linked list
    def deleteAtLast(self):
        if self.is_empty():
            print("List is empty!")
        elif self.head.next is self.head:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = self.head
            self.tail = current   

    #delete a node inside a circular linked list
    def deleteInside(self,data):
        if self.is_empty():
            print("List is empty!")
        else:
            if self.head.item == data:
                self.deleteAtFirst()
            elif self.tail.item == data:
                self.deleteAtLast() 
            else:
                current = self.head
                while current.next is not self.tail:
                    if current.next.item == data:
                        current.next = current.next.next
                        return #exit the loop after deleting the node    
                    current = current.next              
    
 
    def printList(self):
        current = self.head
        print("Circular Linked list is: ",end=" ")
        while current:
            print(current.item,end=" ")
            current = current.next
            if current == self.head:
                break


list = CLL()
list.addFirst(1)
list.addLast(2)
list.addInside(list.search(2),3)
list.addLast(4)
list.printList()
print()
print("Head of Circular Linked List ",list.head.item)
print("Tail of Circular Linked List ",list.tail.item)
print(list.head.next.item)
print(list.tail.next.item)
list.deleteInside(3)
list.printList()
print()
print("Head of Circular Linked List ",list.head.item)
print("Tail of Circular Linked List ",list.tail.item)
print(list.head.next.item)
print(list.tail.next.item)



