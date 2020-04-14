import random
from collections import Counter
four_uniform_randoms = [random.random() for _ in range(4)] #four random numbers from 0 to 1
_, y = [1,2]
print(y)
print(four_uniform_randoms)
random.seed(10) # set internal stage (determinator)
print(random.random())
random.seed(10)
print(random.random())# the same value
x = random.randrange(10); print(x)# randomly select from 0...9
x = random.randrange(3,6); print(x)# randomly select from 3,4,5
up_to_ten = list(range(10))
random.shuffle(up_to_ten)# shuffle randomly
print(up_to_ten)
noname = random.choice(["Snake","Anonym","Mass"])
print(noname)
l_numbers = list(range(60))
w_numbers = random.sample(l_numbers,6) # get random 6 numbers from l_numbers; this method returns distinct elements without repeats
print(w_numbers)
w_numbers.append(random.choice(l_numbers))
print(w_numbers)
print(l_numbers)
del l_numbers[0]
print(l_numbers)
di = {"1" : 1,"22":2}
del di["1"]
print(di)
w_numbers = [random.choice(l_numbers) for _ in range(65)] # new sequence
