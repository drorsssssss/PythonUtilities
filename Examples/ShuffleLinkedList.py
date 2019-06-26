class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def addNode(self,val):
        new_node=Node(val)
        new_node.next = self.head
        self.head=new_node

    def printLinkedList(self):
        start=self.head
        print("Head -> ",end="")
        while start != None:
            print(f"{start.val} -> ",end="")
            start=start.next
        print("")

    def addNodeEnd(self,val):
        start=self.head
        if start is None:
            self.head = Node(val)
        else:

            while start.next != None:
                start=start.next

            start.next=Node(val)

def getSecondHalve(lst):
    start = lst.head
    count=0
    while start != None:
        count+=1
        start=start.next
    middle = int(count/2)

    start_sec = lst.head
    for i in range(middle):
        start_sec=start_sec.next

    f=lst.head
    for i in range(middle-1):
        f=f.next
    f.next=None
    return LinkedList(start_sec)

def mixLists(first,second):
    result=LinkedList()
    while first != None:
        result.addNodeEnd(second.val)
        result.addNodeEnd(first.val)
        first=first.next
        second=second.next
    return result


def shuffleLinkedList(lst):
    second= getSecondHalve(ls)
    result = mixLists(lst.head,second.head)
    result.printLinkedList()



ls = LinkedList()
ls.addNode(6)
ls.addNode(7)
ls.addNode(8)
ls.addNode(9)
ls.addNode(10)
ls.addNode(12)

print("Before shuffle:")
ls.printLinkedList()
print("Shuffled:")
shuffleLinkedList(ls)




