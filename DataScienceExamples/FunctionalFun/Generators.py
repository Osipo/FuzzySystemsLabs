nums = [x for x in range(10)] # list 0..9
print(nums)
cnums = [x*x for x in range(10) if x % 2 == 0] # list of squares of even numbers
nums = [(x,y) for x in range(10) for y in range(x+1, 10)]
print("unique tuples x < y")
print(nums)
print("Squares of even numbers")
print(cnums)
dict = {x:x*x for x in range(10)} # dictionary
print("Squares from 0 to 9")
print(dict)
square_set = {x*x for x in[1,-1]} # set
print("Set of squares 1")
print(square_set)
def natural(n):
    i = 1
    while i<n:
        yield i
        i+=1
li = list((i for i in natural(20)))
print(li)