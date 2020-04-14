import numpy as np
import time as t
from DataScienceExamples.Data.User import *
def queries(n):
    i = 0
    while i < n:
        date = t.localtime(t.time())
        yield ({"id" : hash(i)},i,"Created in %d.%d.%d %d:%d:%d" %(date[2],date[1],(date[0]),date[3],date[4],date[5]))
        i+=1

uss = list((i for i in queries(20)))
print(uss)