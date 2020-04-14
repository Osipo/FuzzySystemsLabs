import math
class Point:
    def __init__(self,x=0,y=0,color='b'):
        self.x = x
        self.y = y
        self.color = color

    def setX(self,x=0):
        self.x = x;

    def setY(self,y=0):
        self.y = y;

    def getX(self):
        return self.x;

    def getY(self):
        return self.y;

    def getCoords(self):
        return [self.x,self.y];

    def distance(self,p):
        if(p is None or not(isinstance(p,Point))):
            raise SyntaxError("Error! Argument is required: Point p")
        return math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2);

    def setCenter(self,p):
        if(p is None or not(isinstance(p,Point))):
            raise SyntaxError("Error! Argument is required: Point p")
        self.c = p;

    def getCenter(self):
        return self.c

    def __repr__(self):
        return 'Point('+str(self.x)+', '+str(self.y)+')\n';

    def __add__(self, other):
        if (other is None or not (isinstance(other, Point))):
            raise SyntaxError("Error! Argument is required: Point p")

        p = Point(self.x+other.getX(),self.y+other.getY()); # new point with old_x + other_x, old_y + other_y
        return p

    def __mul__(self, other):
        return Point(self.x*other,self.y*other);

    def __truediv__(self, other):
        if(self.x % 1 == 0 and self.y % 1 == 0):
            return Point(self.x//other, self.y//other) # integral division
        return Point(self.x/other, self.y/other) # divides coords on other and return them.

    def getColor(self):
        return self.color;
    def setColor(self,color):
        self.color = color;