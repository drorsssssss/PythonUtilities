'''Implementation of undirected graph (Lists)'''

'''Class node'''

class Node:
    def __init__(self,vertex):
        self.vertex=vertex
        self.next=None

'''Class Graph'''

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.root=[None]*self.V

    def add_edge(self,src,dest):

        #Adding dest into src
        node=Node(dest)
        node.next=self.root[src]
        self.root[src]=node

        #Adding src into dest
        node=Node(src)
        node.next=self.root[dest]
        self.root[dest]=node

    def printGraph(self):
        for i in range(len(self.root)):
            temp=self.root[i]
            if not temp:
                continue
            print(f"Vertex: {i} \n head", end="")
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp=temp.next
            print("\n")    