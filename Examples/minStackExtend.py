from copy import copy

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=Node()

    def push(self,element):
        n=Node(element)
        n.next=self.top
        self.top=n

    def pop(self):
        res=self.top
        self.top=self.top.next

        return res.data


    def peek(self):
        return self.top.data

    def isEmpty(self): return self.top is None


class StackMin(Stack):
    def __init__(self):
        self.minTop=Node()
        super().__init__()


    def push(self,data):
        super().push(data)
        if self.minTop.data is None or data < self.minTop.data:
            n=Node(data)
            n.next=self.minTop
            self.minTop=n

    def pop(self):
        return Stack.pop(self)

    def peek(self):
        return Stack.peek(self)

    def isEmpty(self):
        return Stack.isEmpty(self)






st =StackMin()

st.push(20)
st.push(10)
st.push(30)
st.push(5)
st.push(40)

print()