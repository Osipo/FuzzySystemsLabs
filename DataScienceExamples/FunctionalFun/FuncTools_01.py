from functools import partial
from functools import reduce
import random
def exp(base,power):
    return base ** power

"""Функция partial(f,arg) Принимает функцию f и связывает первый аргумент arg с ней, возвращает связанную функцию
Аргументы можно связывать по ключю. Ключ здесь является именем аргумента функции f.
"""
two_exp = partial(exp,2)# first argument of exp
square_of = partial(exp,power=2)# argument power of exp
print(two_exp(3))
print(square_of(3))
def double(x):
    return x * 2
xs = [1,2,3,4]
twice_xs = list([double(x) for x in xs])# [2,4,6,8] using generators
twice_xs = list(map(double,xs))# using map function
doubler = partial(map,double)# using partial function -> map(f,list) => map(<double>,list)
twice_xs = list(doubler(xs))# map(double,xs)
print(twice_xs)

def isEven(x):
    return x&1 == 0
xs = list(range(10))
x_evens = list([x for x in xs if isEven(x)]) # Generators
print(x_evens)
x_evens = list(filter(isEven,xs)) # using filter function
print(x_evens)
list_evener = partial(filter,isEven) # using partial function
x_evens = list(list_evener(xs))
print(x_evens)

def mul(x,y):
    return x*y
data = list(range(1,101))
#random.shuffle(data)
squares = partial(reduce,mul)# reduce(mul,...)
mdata = squares(data)
mdata_2 = reduce(mul,data)
print(data)
print("Index element")
for i, el in enumerate(data):
    print(i,el)
#only indexes
print("Indexes")
for i, _ in enumerate(data):
    print(i)
print(mdata)
print(mdata_2)