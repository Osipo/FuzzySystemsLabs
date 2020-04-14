import math
subs = {str(x)+''+str(y):str(x-y) for x in range(0,10) for y in range(0,10)}
nums = {str(x):str(x) for x in range(0,10)}
simplesc = {}
def compare(ar1,ar2):
    if not(isinstance(ar1,str) and isinstance(ar2,str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0 and len(ar2)>0):
        raise AttributeError('No empty str are required!')
    k = 0
    if (ar1[0] == '-'):
        k = 1
    if (ar1[0] == '-' and ar2[0] != '-'):
        return -1
    elif (ar1[0] != '-' and ar2[0] == '-'):
        return 1
    elif(len(ar1)>len(ar2)):
        return 1
    elif(len(ar1)<len(ar2)):
        return -1
    else:
        for i in range(k,len(ar1)):
            r = subs[ar1[i]+ar2[i]]
            if(r[0]=='-'):
                return -1
            elif(r[0]!='0'):
                return 1
            else:
                continue
    return 0

def isZero(ar1):
    if not(isinstance(ar1,str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0):
        return True
    for i in range(0,len(ar1)):
        if ar1[i]=='.':
            continue
        if ar1[i]!='0':
            return False
    return True

def isNumber(s):
    if not(isinstance(s,str)):
        raise TypeError('Only str attributes!')
    if s in nums:
        return True
    return False

def isSimple(num):
    simples = {}
    if num & 1 == 0: # Even
        return False
    i = 3
    r = math.sqrt(num)
    for n in simplesc:
        if num % n == 0:
            return False
    while(i<=r):
        if num % i == 0:
            return False
        i+=2
    def internal(): # Capture F
        simples[num] = num # Save Simple
        simplesc = simples # Copy from F to the P
        return True
    return internal()

def overturn(ar1):
    if not (isinstance(ar1, str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0):
        raise AttributeError('No empty str is required!')
    an = ''; i = len(ar1)
    while(i>0):
        i-=1
        an+=ar1[i]
    return an
