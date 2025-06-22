'''Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def printList(self):
        if not self.head:
            print("List is Empty")
            return
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
    
    def deleteNthNode(self, n):
        # Edge Cases:-
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        if n<=0:
            raise  Exception("Index should be greater than or equal to 1")
        if n==1:
            print(f"Deleting node at position {n} with value {self.head.data}")
            self.head = self.head.next
            return
        
        temp = self.head
        count = 1
        while temp and count<n-1:
            temp = temp.next
            count+=1

        if not temp or not temp.next:
            raise Exception("Index out of range")
        
        print(f"Deleting node at position {n} with value {temp.next.data}")
        temp.next = temp.next.next

l1 = LinkedList()
l1.addNode(10)
l1.addNode(20)
l1.addNode(30)
l1.addNode(40)

print("Initial list:")
l1.printList()
l1.deleteNthNode(4)
l1.printList()
