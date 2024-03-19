#from typing import Any


class Node:
    def __init__(self,data):
        self.item = data
        self.next = None


class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None
    
                   # no such element found
    
    def search(self,data):
        current = self.head
        while (current != self.tail):
            if (current.item == data):
                return current
            current = current.next
            if current is self.tail:
                return current
        return None        

        
        
    #inserting a node at the starting of the circular linked list
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode

        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.head = newNode

    #inserting a node inside the circular linked list
    def insertInside(self,current,data):
        if current is None:
            print("Node is not found in the list")
            return
        else:
            newNode = Node(data)            
            newNode.next = current.next            
            current.next = newNode
            if current is self.tail:
                self.tail = newNode

            
    #inserting a node at the starting of the circular linked list
    def insertAtLast(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:             
             newNode.prev = self.tail   
             newNode.next = self.head  
             self.tail.next = newNode  
             self.tail = newNode       
           
    
    #deleting a node from starting of the linked linked list
    def deleteAtFirst(self):
        if self.is_empty():
            print("List is empty!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    #deleting a node inside the circular linked list
    def deleteInsideList(self,data):
        if self.is_empty():
            print("List is empty!")
        elif self.head.item == data:
            self.deleteAtFirst()
        else:
            current = self.head
            while current is not self.tail:
                if current.next.item == data:
                    if current.next is self.tail:
                        current.next = self.head
                        self.tail = current
                    else:
                        current.next = current.next.next                        
                    break #exit the loop after deleting the node 
                current = current.next     
      

    #deleting a node from the last of the circular linked list    
    def deleteAtLast(self):
        if self.is_empty():
            print("list is empty!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = self.head
            self.tail = current
            
                
            
    def display(self):
        current = self.head
        if not self.is_empty():
            print("Circular Linked List is :",end=" ")
            while True:
                print(current.item,end=" ")
                current = current.next
                if current == self.head:
                    break          


list = CLL()
list.insertAtStart(1)
list.insertAtLast(2)
list.insertAtLast(3)
#list.display()
list.insertInside(list.search(3),500)
list.display()
print()
print("Head of Circular Linked List is ",list.head.item)
print("Tail of Circular Linked List is ",list.tail.item)

list.deleteInsideList(3)
list.display()
print()
print("Head of Circular Linked List is ",list.head.item)
print("Tail of Circular Linked List is ",list.tail.item)












    
