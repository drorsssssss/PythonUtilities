#Define a Node class

class Node():
    def __init__(self,value):
        self.__value=value
        self.__next=None

    def getValue(self):
        return self.__value

    def getNext(self):
        return self.__next

    def setValue(self,newValue):
        self.__value=newValue

    def setNext(self,nextNode):
        self.__next=nextNode


    # Define LinkedList class

class LinkedList():
    def __init__(self):
        self.__head=None

    def insert(self,newValue):
        newNode = Node(newValue)

        if self.__head is None:
            self.__head=newNode
        else:
            newNode.setNext(self.__head)
            self.__head=newNode
    def getHead(self):
        return self.__head

    def delete(self,value):
        currentNode=self.__head

        while currentNode is not None:

            if currentNode.getValue() == value and currentNode==self.__head:
                self.__head=currentNode.getNext()
                break

            elif currentNode.getNext() and currentNode.getNext().getValue() == value:
                currentNode.setNext(currentNode.getNext().getNext())
                break


            currentNode=currentNode.getNext()

    def traverse(self):
        currentNode=self.__head
        while currentNode is not None:
            print(f"Current value:{currentNode.getValue()} Next node value: {currentNode.getNext().getValue() if currentNode.getNext() else None}")
            currentNode=currentNode.getNext()

    def size(self):
        currentNode=self.__head
        count=0
        while currentNode is not None:
            count+=1
            currentNode=currentNode.getNext()
        return count






