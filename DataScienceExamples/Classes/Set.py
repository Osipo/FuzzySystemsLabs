class Set:
    c = 0
    def __init__(self,values=None):
        self.dict = {}
        self.length = 0
        if values is not None:
            for value in values: self.add(value)

    def add(self,value):
        self.dict[value] = True
        self.length+=1

    """Overrides toString() or str() """
    def __repr__(self):
        return "Set: "+str(self.dict.keys())

    def contains(self,value):
        return value in self.dict

    def remove(self,value):
        del self.dict[value]
        self.length-=1

    """Length of the Set. This method overrides length() or len()"""
    def __len__(self):
        return self.length
s = Set(list(range(10)))
f = float(2.3)
print(f)
d = 0.99_99
print(d)
print("f is Float : "+str(isinstance(f,float)))
s.add(11)
print(s.contains(11))
s.remove(11)
print(s.contains(11))
print(s.contains(5))
print(s)
s.remove(5)
print(s)
print(len(s)) # length = 9