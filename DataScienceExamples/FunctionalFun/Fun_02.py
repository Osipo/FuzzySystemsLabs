data = list(range(1,101))
print(data)
print("Index element")
for i, el in enumerate(data):
    print(i,el)
#only indexes
print("Indexes")
for i, _ in enumerate(data):
    print(i)

li = [1,2,3]; li2 =['a','b','c']
pairs = list(zip(li,li2)) #zip joins two elements from two lists
print(pairs)
unzip = list(zip(*pairs))
unzip1 = list(zip((1,'a'),(2,'b'),(3,'c')))
print(unzip)
print(unzip1)

def sum(x,y):
    return x+y
print(sum(*[1,2])) #3

def magic(*args,**kwargs):
    print("Безымянные аргументы: ",args)
    print("Аргументы по ключю: ",kwargs)

def doubler(f):
    def g(*args, **kwargs):
        return 2 * f(*args,**kwargs) # sum(args,kwargs) * 2
    return g
g = doubler(sum)

@doubler
def mull(a,b):
    return a*b
print(mull(5,2)) # 20
print(g(1,2)) #(1+2)*2
magic(1,2,3,some='nonsense1',key='something',key1=33)
try:
    x = 5/0
except ZeroDivisionError:
    x = 0
finally:
    print(x)
try:
    x = -2
    if(x < 0): raise ValueError('Must be positive')
except ValueError:
    x = 2
finally:
    print(x)

