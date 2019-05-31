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
            print(base.data, end=" ")
            self.__printTree(base.right)

    # PreOrder printing
    def printTreePreOrder(self):
        self.__printTreePreOrder(self.root)

    def __printTreePreOrder(self,base):
        if base:
            print(base.data, end=" ")
            self.__printTreePreOrder(base.left)
            self.__printTreePreOrder(base.right)


    def sum(self):
        return self.__sum(self.root)

    def __sum(self,base):
        if base:
            left = self.__sum(base.left)
            right = self.__sum(base.right) + base.data
            return left + right
        else:
            return 0

    def count(self):
        return self.__count(self.root)

    def __count(self,base):
        if base:
            return self.__count(base.left) + self.__count(base.right) +1
        else:
            return 0

    def isExist(self,data):
        return True if self.__isExist(self.root,data)>0 else False

    def __isExist(self,base,data):
        left=0
        right=0
        if base:
            if base.data==data:
                return 1
            if data<base.data:
                left = self.__isExist(base.left,data)
            if data>base.data:
                right = self.__isExist(base.right,data)
            return left + right
        else:
            return 0



# Unit Testing
def test_display_inorder():
    root=BinaryTree()
    root.insert(1)
    root.insert(3)
    root.insert(2)
    root.insert(10)
    root.insert(8)
    print("InOrder display")
    print("Should be: 1,2,3,8,10")
    print("Result: ",end=" ")
    root.printTree()


def test_display_preorder():
    root=BinaryTree()
    root.insert(1)
    root.insert(3)
    root.insert(2)
    root.insert(10)
    root.insert(8)
    print("PreOrder display")
    print("Should be: 1,2,3,8,10")
    print("Result: ",end=" ")
    root.printTree()

def test_sum():
    root=BinaryTree()
    root.insert(1)
    root.insert(3)
    root.insert(2)
    root.insert(10)
    root.insert(8)
    assert root.sum() == 24

def test_count():
    root=BinaryTree()
    root.insert(1)
    root.insert(3)
    root.insert(2)
    root.insert(10)
    root.insert(8)
    assert root.count() == 5

def test_isExist():
    root=BinaryTree()
    root.insert(1)
    root.insert(3)
    root.insert(2)
    root.insert(10)
    root.insert(8)
    assert root.isExist(1) == True

pytest.main(["-rA"])