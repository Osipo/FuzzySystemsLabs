import mpmath
import random
class Bits:
    bits = [0]
    def test(self,index):
        return (self.bits[int(mpmath.floor(index/32))] >> index % 32) & 1
    def set(self,index):
        self.bits[int(mpmath.floor(index/32))] |= 1 << (index % 32)

def hash():
    seed = int(mpmath.floor(random.random()*32))+32
    def r(str):
        result = 1
        for i in range(1,len(str)):
            result = (seed * result+ord(str[i])) & 0xFFFFFFFF
        return result
    return r

class BloomFilter:
    funcs = []; size = 0
    def __init__(self,size,funcs):
        self.size = size
        self.funcs = funcs
    bits = Bits()
    def add(self,str):
        for i in range(1,len(self.funcs)):
            self.bits.set(self.funcs[i](str) % self.size)

    def test(self,str):
        for i in range(1,len(self.funcs)):
            if not(self.bits.test(self.funcs[i](str) % self.size)): return False
        return True
fruits = BloomFilter(64,[hash(),hash()])
fruits.add('apple');
fruits.add('orange');

