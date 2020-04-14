from DataScienceExamples.Classes import Point
class Rectangle:
    def __init__(self,x1=0,y1=0,x2=10,y2=10):
        self.A = Point.Point(x1,y1)
        self.B = Point.Point(x2,y1)
        self.C = Point.Point(x1,y2)
        self.D = Point.Point(x2,y2)
        self.S = self.getWidth()*self.getHeight()

    def getA(self):
        return self.A
    def getB(self):
        return self.B
    def getC(self):
        return self.C
    def getD(self):
        return self.D

    def getWidth(self):
        return self.B.getX()-self.A.getX()

    def getHeight(self):
        return self.C.getY() - self.A.getY()

    def getSquare(self):
        return self.S

    def getPoints(self):
        return [self.A,self.B,self.C,self.D]
    def __repr__(self):
        return 'Rectangle(\n\t'+'P1: '+str(self.A.getX())+', '+str(self.A.getY())+')\n\t'+'P2: '+str(self.B.getX())+', '+str(self.B.getY())+'\n\t'+'P3: '+str(self.C.getX())+', '+str(self.C.getY())+'\n\t'+'P4: '+str(self.D.getX())+', '+str(self.D.getY())+'\n)';