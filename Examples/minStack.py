from copy import copy

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=Node()
        self.minTop=Node()

    def push(self,element):
        n=Node(element)
        n.next=self.top
        self.top=n

        if self.minTop.data is None or self.minTop.data>n.data:
            newMin = copy(n)
            newMin.next=self.minTop
            self.minTop=newMin

    def pop(self):
        res=self.top
        self.top=self.top.next

        if res.data == self.minTop.data:
            self.minTop=self.minTop.next
        return res.data


    def peek(self):
        return self.top.data

    def isEmpty(self): return self.top is None

    def getMin(self): return self.minTop.data



st = Stack()

st.push(20)
st.push(10)
st.push(30)
#st.push(5)
#st.push(40)

print()