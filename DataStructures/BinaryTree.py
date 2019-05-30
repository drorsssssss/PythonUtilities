import pytest

# Define Node Class

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

#Define Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root=Node(None)

    def insert(self,data):
        self.__insert(self.root,data)

    def __insert(self,base,data):
        if base.data:
            if data<=base.data:
                if base.left:
                    self.__insert(base.left,data)
                else:
                    base.left=Node(data)
            else:
                if base.right:
                    self.__insert(base.right,data)
                else:
                    base.right=Node(data)

        else:
            base.data=data

    # InOrder printing
    def printTree(self):
        self.__printTree(self.root)

    def __printTree(self,base):
        if base:
            self.__printTree(base.left)
            if base is not None:
                print(base.data)
            self.__printTree(base.right)



class TestBinaryTree:
    def __init__(self):
        self.root=BinaryTree()

    def test_insert(self):
        self.root.insert(1)
        self.root.insert(3)
        self.root.insert(2)
        self.root.insert(10)
        self.root.insert(8)
        print("InOrder display")
        self.root.printTree()


        