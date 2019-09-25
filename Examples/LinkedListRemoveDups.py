class Node:
    data=None
    next=None

    def __init__(self,val):
        self.data=val

class LinkedList:
    head=None

    def insert(self,val):
        n = Node(val)
        n.next=self.head
        self.head=n

    def printLinkedList(self):
        print("")
        start=self.head
        print("Head -> ",end="")
        while start!=None:
            print(f"{start.data} -> ",end="")
            start=start.next
        print("None",end="")

    def removeDups(self):
        start=self.head
        while start!=None:
            curr=start.next
            prev=start
            while curr !=None:
                if start.data == curr.data:
                    prev.next=curr.next
                else:
                    prev=curr
                curr=curr.next
            start=start.next

    def cnt(self,head):
        if head is None:
            return 1
        return self.cnt(head.next) +1



ll = LinkedList()
ll.insert(1)
#ll.insert(1)
ll.insert(2)
ll.insert(1)
ll.insert(1)
ll.printLinkedList()
ll.removeDups()
ll.printLinkedList()
print("")
print(ll.cnt(ll.head))

