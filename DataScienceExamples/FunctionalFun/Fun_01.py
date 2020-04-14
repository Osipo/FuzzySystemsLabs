def inc(x=0):
    return x+1
f = lambda x,y: x+y
print(inc(f(2,5)))
print(inc())
o = {"id":2,"name":"John Senna"}
co = [x,y] = o
print(co)
def sum_and_mul(x,y):
    return (x+y),(x*y)
a,b = sum_and_mul(5,5)
print(a,b)
l ="some" if a == 0 else "none" "event" if a % 2 == 0 else 1 if a < 0 else 0  #  (P  P1 A1: B1 : B)
print(l)