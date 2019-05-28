# Define Trie Node class

class TrieNode():
    def __init__(self):
        self.isWord=False
        self.children={}


    def getChildByKey(self,key):
        return self.children[key] if key in self.children else None

    def getIsWord(self):
        return self.isWord

    def setChild(self,key):
        self.children[key] = TrieNode()

    def setIsWord(self,exp):
        self.isWord=exp

    def printTrieNodeData(self):
        print(f"isWord: {self.isWord}, Children: {self.children}")


# Define a Trie class

class Trie():
    def __init__(self):
        self.root=TrieNode()

    def getTrieRoot(self):
        return self.root

    def insert(self,word):
        currentNode = self.getTrieRoot()
        cnt=0
        for letter in word:
            cnt+=1
            if letter not in currentNode.children:
                currentNode.setChild(letter)

            currentNode.printTrieNodeData()
            currentNode=currentNode.getChildByKey(letter)

        currentNode.isWord=True
        currentNode.printTrieNodeData()









