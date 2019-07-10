class kv:
    key=None
    value=None

class HashTable:
    def __init__(self):
        self.arr=[kv()]
        self.numElements=0

    def getAsciiVal(self,st):
        st=str(st)
        sum=0
        for char in st:
            sum+=ord(char)
        return sum

    def hashingFunc(self,key):
        return self.getAsciiVal(key) % len(self.arr)

    def insert(self,key,value):

        print(f"Load factor: {self.loadFactor()}")
        if self.loadFactor()>=0.75:
            self.arr.extend([kv() for _ in range(len(self.arr))])
        index = self.hashingFunc(key)
        i=1
        while ((self.arr[index].key!=None and self.arr[index].key!=key) and i<=len(self.arr)):
            index=(index+pow(i,2)) % len(self.arr)
            i+=1

        self.arr[index].key=key
        self.arr[index].value=value
        self.numElements+=1

        for index in self.arr:
            print(f"({index.key},{index.value})", end=" ")

    def get(self,key):
        index=self.hashingFunc(key)
        i=1
        while (self.arr[index].key!=key and i<=len(self.arr)):
            index=(index+pow(i,2)) % len(self.arr)
            i+=1
        return self.arr[index].value if self.arr[index].key==key else None

    def loadFactor(self):
        return 1.0*self.numElements/len(self.arr)

x=HashTable()
x.insert(5,6)
print("")
x.insert(1,2)
print("")
x.insert(4,6)
print("")
x.insert(10,33)
print("")

x.insert(7,88)
print("")
x.insert(6,333)
print("")
print(x.get(10))



