import random
def random_kid():
    return random.choice(["boy","girl"])

b_girls = 0
older_girls = 0
either_girl = 0
random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girls+=1
    if older == "girl" and younger == "girl":
        b_girls+=1
    if older == "girl" or younger == "girl":
        either_girl+=1
print('P(Both|Older_girl): ',b_girls/older_girls)
print('P(Both|Any_girl): ',b_girls/either_girl)