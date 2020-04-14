from DataScienceExamples.Data.NumbersProperties import compare
from DataScienceExamples.Data.NumbersProperties import isZero
adds = {str(x)+''+str(y):str(x+y) for x in range(0,10) for y in range(0,10)}
muls = {str(x)+''+str(y):str(x*y) for x in range(0,10) for y in range(0,10)}
subs = {str(x)+''+str(y):str(x-y) for x in range(0,10) for y in range(0,10)}
dsubs = {'1'+str(x)+''+str(y):str((10+x)-y) for x in range(0,10) for y in range(0,10)}
print(adds)
print(muls)
print(subs)
print(dsubs)

def longstr(s1,s2,reverse=False):
    if(reverse):
        return (reversed(s1),reversed(s2)) if(len(s1)>=len(s2)) else (reversed(s2),reversed(s1))
    else:
        return (s1,s2) if(len(s1)>=len(s2)) else (s2,s1)

def fillzeroes(r1,r2):
    i = 0
    k = len(r1)-len(r2)
    if(k>0):
        while(i<k):
            r2+='0'
            i+=1
    elif(k<0):
        while(i>k):
            r1+='0'
            i-=1
    return r1,r2

def dropzeroes(r,reverse=True):
    i = len(r)-1; an = ''
    if(reverse):
        while(i>=0):
            if(r[i]!='0'):
                if(i==0): an = r[0]; break
                an+= r[0:i+1]
                break
            i-=1
        if len(an)==0: an = '0'
    else:
        i = 0
        while(i<len(r)):
            if(r[i]!='0'):
                an+= r[i:]
                break
            i+=1
    return an

def zeroone(num): #is 01, 001, 0001....
    i = 0
    while(i<len(num)-1):
        if num[i]!='0':
            return False
        i+=1
    return True if num[i]=='1' and i>0 else False

def backtoint(n1,n2,r1,r2):
    i = 0
    k = len(r1)-len(r2)
    if(n1=='0'):
        n1 = ''
    if(n2=='0'):
        n2 = ''
    if(k>=0): # r1 more floatable
        while(i<len(r1)):
            n1+=r1[i] if i<len(r1) else '0'
            n2+=r2[i] if i<len(r2) else '0'
            i+=1
    elif(k<0):
        while(i<len(r2)):
            n1 += r1[i] if i<len(r1) else '0'
            n2 += r2[i] if i<len(r2) else '0'
            i +=1
    i*=2
    return n1,n2,i

def performull(ar1,ar2,table):
    (ar1, ar2) = longstr(ar1, ar2)
    ar2 = list(reversed(ar2))# reversed multiplier
    l1 = len(ar1); l2 = len(ar2); j = 0; i = 0; k = '';b = 0; bb = False; ext = 0
    slogs = []
    if(l1==1 and l2==1): # Simple case: digits.
        return muls[ar1[0]+ar2[0]]
        #128 * 12 = 1536
        #821 * 21
        #592 * 2 = 1184
        #383 * 2 = 766
        #3383 * 2 =
        #999 * 9 = 8991
    res = ''
    while(j<len(ar2)):
        while(i<len(ar1)):
            r = table[ar1[i]+ar2[j]] # 2020 * 5 = 10100
            res += r # 10
            ext = len(res)
            b+=1
            if(len(r)>1):
                if(i==1 and len(res)==4):#592 2  383 2
                    res = addition(res[:i+1],r[0])+r[1]#1018
                else:
                    if(i+3==ext):
                        ext = 0
                        res = addition(res[:i+1],r[0])+r[1]
                    else:
                        res = addition(res[:i],r[0])+r[1]
            i+=1
        res+=k
        k+='0'
        slogs.append(res)
        j+=1
        i = 0
        b = 0
        res = ''
    if(len(slogs)==1):
        return slogs[0]
    else:
        if(len(slogs)==2): return addition(slogs[0],slogs[1])
        else:
            pro = addition(slogs[0],slogs[1])
            for q in range(1,len(slogs)-1):
                pro = addition(pro,slogs[q+1])
            return pro

def perform(ar1,ar2,table):
    (ar1, ar2) = longstr(ar1, ar2)
    l1 = len(ar1); l2 = len(ar2); j = 0; b = 0; bb = False; i = 0;

    while (i < len(ar1)):
        if (l1 > l2):
            l1 -= 1
            i += 1
            continue
        r = table[ar1[i] + ar2[j]]
        while (len(r) > 1):
            if (len(r) > 1 and i == 0):  # first index
                res = r + ar1[i + 1:]  #888+791 = 1588
                ar1 = res
                r = '0'
                b += 2 # how many indexes must be passed to the uncalculated
                j+=1
                bb = True# need back to uncalculated
                break
            res = ar1[:i] + r[1] #
            if(i+1 < len(ar1)): res+=ar1[i+1:] # 1578
            ar1 = res
            bb = True
            i -= 1
            b += 1
            r = table[ar1[i] + r[0]] #1678
            if (len(r) > 1):
                continue
            else:
                res = ar1[:i] + r[0] + ar1[i + 1:] #1679
                ar1 = res
                i += 1
                j += 1
        if (bb):
            i += b
            bb = False
            b = 0
            continue
        res = ar1[:i] + r[0] + ar1[i + 1:]
        ar1 = res
        j += 1
        i += 1
    return res

def subtract(ar1,ar2):
    l1 = len(ar1); l2 = len(ar2); pref = ''; i = 0; j = 0; res = ''; b = 0; bb = False
    if(ar1[0]!='-' and ar2[0]=='-'): # a - (-b) = a + b
        return addition(ar1,ar2[1:])
    elif(ar1[0]=='-' and ar2[0]!='-'):
        return '-'+addition(ar1[1:],ar2) # -a - b = -(a+b)
    elif(ar1[0]=='-' and ar2[0]=='-'):# -a - (-b) = -a + b = b + (-a) = b - a
        return subtract(ar2[1:],ar1[1:])
    elif (compare(ar1, ar2) == 0):
        return '0'
    elif(compare(ar1,ar2)<1):
        pref = '-' # a - b = -(b-a) = -b - a
        tmp = ''
        tmp = ar1
        ar1 = ar2 # ar2 > ar1
        ar2 = tmp if tmp[0]!='-' else tmp[1:] #-b - a = a - b
        l1 = len(ar1)
        l2 = len(ar2)
    while(i<len(ar1)):
        while(l1>l2):
            res+=ar1[i] # 1
            i+=1
            l1-=1
            continue
        r = subs[ar1[i]+ar2[j]] # -7
        if(i>0):
            if(r.startswith('-')):
                if(i-1==0):
                    r = dsubs['1'+ar1[i]+ar2[j]] #109 => 1
                    res = subs[res[i-1]+'1']+r # 01
                    r = ''
                else:
                    # print(res)
                    r = dsubs['1'+ar1[i]+ar2[j]]# 129 => 3
                    s = subs[res[i-1]+'1'] if i-1<len(res) else subs[res[i-2]+'1']
                    old = r
                    # print(old)
                    la = ''
                    while(s[0]=='-' and i>0):
                        i-=1 #330<
                        b+=1
                        bb = True
                        r = dsubs['1'+res[i]+'1'] # 9
                        res = res[:i]+r+res[i+1:]
                        # print(res)
                        s = subs[res[i-1]+'1']
                        # print(s)
                        la = res[len(res)-1]
                    res = res[:i-1]+s+la+old
                    # print(res)
                    r = ''
            else:
                res+=r
                r = ''
        res += r
        if(bb):
            bb = False
            i+=b+1
            b = 0
        else:
            i+=1
        j+=1
    return pref+dropzeroes(res,reverse=False)

def multiplication(ar1,ar2):
    if not(isinstance(ar1,str) and isinstance(ar2,str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0 or len(ar2)>0):
        raise AttributeError('At least one no empty str is required!')
    elif (not (len(ar1) > 0 and len(ar2) > 0) and (len(ar1) > 0 or len(ar2) > 0)): # XOR = AND(NOT(AND(P1,P2)),OR(P1,P2)) = NOT(P1 AND P2) AND (P1 OR P2))
        return ar1 if len(ar1)>0 else ar2
    elif(ar1 == '0' or ar2 =='0'):
        return '0'
    elif(ar1=='1' or ar2=='1'):
        return ar1 if ar2=='1' else ar2

    li = ar1.split('.')
    li2 = ar2.split('.')
    if (len(li) > 1 and len(li2) > 1):
        num1,num2,de = backtoint(li[0],li2[0],li[1],li2[1])
        result = performull(num1,num2,muls)
        if(ar1[0]=='0' or ar2[0]=='0'):
            integer = '0'
            if(len(result)<de):
                result = '0'+result
        else:
            integer = result[0:len(result)-de]
        real = result[len(result)-de:len(result)] if integer!='0' else result[0:]
        return integer+'.'+dropzeroes(real)
    elif (len(li) > 1 and len(li2) < 2):
        num1,num2,de = backtoint(li[0],li2[0],li[1],[])
        result = performull(num1,num2,muls)
        if(ar1[0]=='0' and ar2[0]=='0'):
            integer = '0'
            if (len(result) < de):
                result = '0' + result
        else:
            integer = result[0:len(result) - de]#5 * 0.25 = 500 * 25 = 12500
        real = result[len(result)-de:len(result)] if integer != '0' else result[0:]
        if(zeroone(num1)): real = real[1:]
        if(integer==''):
            integer = '0'
        return integer+'.'+dropzeroes(real)
    elif (len(li) < 2 and len(li2) > 1):
        num1,num2,de = backtoint(li[0],li2[0],[],li2[1])
        result = performull(num1,num2,muls)
        if(ar1[0]=='0' and ar2[0]=='0'):
            integer = '0'
            if (len(result) < de):
                result = '0' + result
        else:
            integer = result[0:len(result) - de]
        real = result[len(result)-de:len(result)] if integer!='0' else result[0:]
        if (zeroone(num2)): real = real[1:]
        if (integer == ''):
            integer = '0'
        return integer+'.'+dropzeroes(real)
    else:
        return performull(ar1,ar2,muls)

def addition(ar1,ar2):
    if not(isinstance(ar1,str) and isinstance(ar2,str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0 or len(ar2)>0):
        raise AttributeError('At least one no empty str is required!')
    elif (not (len(ar1) > 0 and len(ar2) > 0) and (len(ar1) > 0 or len(ar2) > 0)): # XOR = AND(NOT(AND(P1,P2)),OR(P1,P2)) = NOT(P1 AND P2) AND (P1 OR P2))
        return ar1 if len(ar1)>0 else ar2

    li = ar1.split('.') #integer and real part of s1
    li2 = ar2.split('.')# integer and real part of s2
    if(len(li)>1 and len(li2)>1):
        pref = perform(li[0],li2[0],adds) #add integer parts
        r1,r2 = fillzeroes(li[1],li2[1]) # make the real parts are equal by the length (0.3, 0.71) -> (0.30,0.71)
        incr = len(r1)
        after = perform(r1,r2,adds) # add real parts
        if(len(after)>incr): # real parts
            pref = addition(pref,after[0])
            after = after[1:]
        return pref+'.'+dropzeroes(after)
    elif(len(li)>1 and len(li2)<2): # s1 = float, s2 = integer
        pref = perform(li[0],li2[0],adds) # integer
        after = pref+'.'+li[1] # from s1 float
        return dropzeroes(after)
    elif(len(li)<2 and len(li2)>1): # s1 = integer, s2 = float
        pref = perform(li[0],li2[0],adds) # integer
        after = pref+'.'+li2[1]
        return dropzeroes(after)
    else: # s1,s2 = integer
        return perform(ar1,ar2,adds)

def subtraction(ar1,ar2):
    if not(isinstance(ar1,str) and isinstance(ar2,str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0 or len(ar2)>0):
        raise AttributeError('At least one no empty str is required!')
    elif (not (len(ar1) > 0 and len(ar2) > 0) and (len(ar1) > 0 or len(ar2) > 0)): # XOR = AND(NOT(AND(P1,P2)),OR(P1,P2)) = NOT(P1 AND P2) AND (P1 OR P2))
        return ar1 if len(ar1)>0 else '-'+ar2

    qq = ''
    li = ar1.split('.')  # integer and real part of s1
    li2 = ar2.split('.')  # integer and real part of s2
    if (ar1[0]=='-' and ar2[0] != '-'):
        return '-'+addition(ar1[1:],ar2)
    elif (ar1[0]!='-' and ar2[0] == '-'):
        return addition(ar1,ar2[1:])
    elif (ar1[0]=='-' and ar2[0]=='-'):
        qq = '-'
    if (len(li) > 1 and len(li2) > 1): # float - float
        pref = subtract(li[0],li2[0])
        r1, r2 = fillzeroes(li[1], li2[1]) # to the same length (0.3, 0.30001) -> (3,30001) -> (30000,30001)
        dicr = len(r1)
        after = subtract(r1,r2)
        adicr = len(after)
        # print(after)
        if(after[0]=='-' and pref[0]!='-'):
            if(pref[0]=='0'):
                pref = '-'+pref
                after = after.replace('-','0')
            else:
                pref = subtract(pref,'1')
                after = after[1:]
            if(adicr-1!=dicr): # minus pass
                while(adicr<dicr):
                    after = '0'+after
                    adicr+=1
        elif(pref[0]=='-' and after[0]=='-'): # 0.5  - 1.7 = -1.2
            after = after[1:]
            pref = '-'+addition(pref[1:],'1')
        else:
            if (adicr != dicr):
                pz = ''
                while(adicr<dicr):
                    pz +='0'
                    adicr+=1
                after = pz + after
        return qq+pref+'.'+after
    elif(len(li)>1 and len(li2)<2): # float - integer
        pref = subtract(li[0],li2[0])
        real = li[1]
        return pref+'.'+real
    elif(len(li)<2 and len(li2)>1): # integer - float
        pref = subtract(li[0],li2[0])
        if(isZero(ar2)):
            return pref
        pref = subtract(pref,'1') if pref[0]!='-' else pref
        r1,r2 = fillzeroes('1',li2[1])
        if(compare(r1,r2)<0):
            r1+='0'
        elif(r2[0]=='0'):
            r1+='0'
        real = subtract(r1,r2)
        return pref+'.'+real
    else:
        return subtract(ar1,ar2)