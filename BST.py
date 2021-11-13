# binary search tree

from collections import deque

class Node:
    def __init__(self, val):
        self.value = val
        self.leftchild = None
        self.rightchild = None

    def insert(self, data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
                return True
    def find(self,data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftchild:
                    self.leftchild.preorder()
            if self.rightchild:
                self.rightchild.preorder()
    
    def inorder(self):
        if self:
            if self.leftchild:
                    self.leftchild.inorder()
            print(str(self.value))
            if self.rightchild:
                self.rightchild.inorder()  
                
    def iterLayers(self):
        q = deque()
        q.append(self)
        def layerIterator(layerSize):
            for i in range(layerSize):
                n = q.popleft()
                if n.leftchild: q.append(n.leftchild)
                if n.rightchild: q.append(n.rightchild)
                yield n.value
        while (q):
            yield layerIterator(len(q))

    def printByLayer(self):
        for layer in self.iterLayers():
            print(' '.join([str(v) for v in layer]))

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preorder(self):
        print('preorder')
        self.root.preorder()
    
    def inorder(self):
        print('inorder')
        self.root.inorder()
        
    def printByLayer(self):
        self.root.printByLayer()
if __name__== "__main__":
    bst = Tree()
    bst.insert(7)
    bst.insert(3)
    bst.insert(18)
    bst.insert(10)
    bst.insert(22)
    bst.insert(8)
    bst.insert(11)
    bst.insert(26)

    bst.printByLayer()






