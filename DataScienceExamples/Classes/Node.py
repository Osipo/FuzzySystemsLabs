class Node:
    def __init__(self,l=0,r=0,p=0.0):
        self.left = None
        self.right = None
        self.symbol = 0
        self.frequency = 0
        self.probability = 0.0
        if(l,r,p is not None and isinstance(l,Node) and isinstance(r,Node)):
            self.left = l
            self.right = r
            self.probability = p

    def setSymbol(self,s):
        self.symbol = s

    def setFrequnecy(self,f):
        self.frequency = f

    def setProbability(self,p):
        self.probability = p

    def getProbability(self):
        return self.probability

    def getSymbol(self):
        return self.symbol

    def getFrequency(self):
        return self.frequency

    def setLeftSon(self,l):
        self.left = l

    def setRightSon(self,r):
        self.right = r

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def __repr__(self):
        return 'Node('+str(self.symbol)+','+str(self.frequency)+')'