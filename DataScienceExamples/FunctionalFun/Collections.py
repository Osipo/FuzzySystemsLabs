from collections import defaultdict
from collections import Counter
words =['a','b','a','a','c','v','b'] # list
print(len(words)) # length of the list words == 7
words.extend([1,2,3,4,5])
print(len(words)) # add numbers 1..5 length == 12
d_words = Counter(words) # dictionary where keys are words and the values are frequencies
for w, c in d_words.most_common(2): # arg == counts of words with max frequencies.
    print(w,c)
d = defaultdict(int) # apply function if key is not exists apply this function  int returns zero (0) list
nums = [-4,1,3,-1,2]
snums = sorted(nums,key=abs,reverse=True)#kwargs: key -> comparator,  reverse -> True or False
print(snums)
dd = defaultdict(dict) # returns empty dictionary
dd["Jon"]["Shepard"] = 'soldier'
print(dd["Jon"])
dd = defaultdict(lambda : [0,0])
dd[0][1] = 1
print(dd[0])