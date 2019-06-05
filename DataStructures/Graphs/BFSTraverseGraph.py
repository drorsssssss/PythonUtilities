from collections import defaultdict,deque


class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.root=defaultdict(list)

    def add_edge(self,src,dest):
        self.root[src].append(dest)

    def BFS(self,start):
        visited=defaultdict(lambda: False)
        queue=deque()
        queue.append(start)
        visited[start]=True

        while queue:
            member = queue.popleft()
            print(member,end=" ")

            for neighbor in self.root[member]:

                if not visited[neighbor]:

                    queue.append(neighbor)
                    visited[neighbor]=True



if __name__ == "__main__":
    x=Graph(4)
    x.add_edge(0,1)
    x.add_edge(0,2)
    x.add_edge(1,2)
    x.add_edge(2,0)
    x.add_edge(2,3)
    x.add_edge(3,3)
    x.BFS(2)        