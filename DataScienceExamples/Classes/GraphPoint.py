class GraphPoint:
    def __init__(self,w = 0):
        self.weight = w
        self.others = []
    def distance(self,gp):
        if(gp is None or not(isinstance(gp,GraphPoint))):
            raise TypeError('Expect GraphPoint instance')
        return gp.getW() - self.weight

    def getW(self):
        return self.weight
    def setW(self,w):
        self.weight = w

    def Neighbours(self):
        return self.others
    def addNeighbour(self,gp):
        self.others.append(gp)