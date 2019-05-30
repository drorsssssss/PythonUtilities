import pytest

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
        for letter in word:
            if letter not in currentNode.children:
                currentNode.setChild(letter)

            currentNode.printTrieNodeData()
            currentNode=currentNode.getChildByKey(letter)

        currentNode.isWord=True
        currentNode.printTrieNodeData()


    def search(self,word):
        currentNode=self.getTrieRoot()
        for letter in word:

            if not currentNode.getChildByKey(letter):
                return False
            currentNode=currentNode.getChildByKey(letter)

        return True if currentNode.isWord else False



    def remove(self,word):
        node = self.getTrieRoot()
        self.__remove(word,node,0)

    def __remove(self,word,node,cnt):

        if cnt == len(word):
            node.setIsWord(False)
            if len(node.children)==0:
                return 1
            else:
                return 0


        result = self.__remove(word,node.getChildByKey(word[cnt]),cnt+1)
        print(f"Result: {result}, Step number {cnt}, letter: {word[cnt]}, Children: {node.printTrieNodeData()}/n")
        if result and len(node.children)<=1 and node.getIsWord() == False:
            node.children.clear()
            return 1
        elif result and len(node.children)<=1 and node.getIsWord() == True:
            node.children.clear()
            return 0
        else:
            return 0

class TestTries():
    def __init__(self):
        self.tr=Trie()




    def test_insert(self):
        word="dror"
        self.tr.insert(word)
        h=self.tr.getTrieRoot()
        c=0
        for i in word:
            if i in h.children:
                c+=1
                h=h.children[i]
            else:
                break

        assert c == 4









        