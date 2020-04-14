from DataScienceExamples.Data.AdditionMultiplicationTables import subtract
from DataScienceExamples.Data.NumbersProperties import compare
from DataScienceExamples.Data.AdditionMultiplicationTables import dropzeroes
from DataScienceExamples.Data.AdditionMultiplicationTables import multiplication
def inverseNumber(ar1,p=1):
    if not(isinstance(ar1,str) and isinstance(p,int)):
        raise TypeError('Only str attribute and int precision!')
    if not(len(ar1)>0 and p>0):
        raise AttributeError('No empty str is required and only positive precision which is greater than zero is permitted!')
    sign = ''
    if(ar1[0]=='-'):
        ar1 = ar1[1:]
        sign = '-'
    ini = '10'; an = '0.'  #1/number
    l = len(ar1)
    i = 1; j = 0; q = 0
    while (i < l): #25 - 100  0.0
        ini += '0'
        an += '0'
        i += 1
    r = ini
    per = r  # the head of period for periodic numbers
    i = 0
    while(ini!='00'):# has remainder
        while(compare(r,ar1)>=0):# can divide
            r = subtract(r,ar1)
            j+=1# 25 - 4.
        an+=str(j) # 0.04
        ini = r+'0'
        print(ar1 + ':  ' + str(ini))
        if(ini=='00'): # end
            break
        i = 0
        while (compare(ini,ar1)<0):
            ini += '0'
            an += '0'
            i += 1
        r = ini
        j = 0
        if(r==per):
            q+=1
        if(q>=p):
            break
    return sign+dropzeroes(an)

def dividertoint(ar1,ar2):
    if not(isinstance(ar1,str) and isinstance(ar2,str)):
        raise TypeError('Only str attribute and int precision!')
    if not(len(ar1)>0 and len(ar2)>0):
        raise AttributeError('No empty str are required!')
    li1 = ar1.split('.')
    num = li1[0]; numr = ''
    if(len(li1)==2):
        numr = li1[1]
    li2 = ar2.split('.')
    if(len(li2)==1):
        return ar1,ar2

    ds = len(li2[1])
    integer = li2[0]
    real = li2[1]
    i = 0
    d = '' if integer=='0' else integer
    while(i<ds):
        d+= real[i]
        num+=numr[i] if i<len(numr) else '0'
        i+=1
    if(i<len(numr)):
        num+='.'
    while(i<len(numr)):
        num+=numr[i]
        i+=1
    return num,d

def division(ar1,ar2):
    if not(isinstance(ar1,str) and isinstance(ar2,str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0 or len(ar2)>0):
        raise AttributeError('At least one no empty str is required!')
    elif (not (len(ar1) > 0 and len(ar2) > 0) and (len(ar1) > 0 or len(ar2) > 0)): # XOR = AND(NOT(AND(P1,P2)),OR(P1,P2)) = NOT(P1 AND P2) AND (P1 OR P2))
        return ar1 if len(ar1)>0 else ar2 # Neitral means 1
    elif(ar1 == '0' and ar2 !='0'):
        return '0'
    elif(ar1 =='0' or ar2=='0'):
        raise ArithmeticError('Undefined!')
    ar1,ar2 = dividertoint(ar1,ar2)
    ar2 = inverseNumber(ar2)
    return multiplication(ar1,ar2)

def binary(ar1):
    if not (isinstance(ar1, str)):
        raise TypeError('Only str attributes!')
    if not(len(ar1)>0):
        raise AttributeError('No empty str is required!')
    elif(len(ar1)==1 and ar1[0]=='0'):
        return '0'

    li = ar1.split('.')
    num = li[0]
    r = num
    ans = ''
    while(r[0]!='0' or len(r)!=1):
        r =  division(r,'2')
        l = r.split('.')
        re = l[1]
        if(re[0]=='0'):
            ans+='0'
            r = l[0] # 64
        else:
            ans+='1'
            r = l[0]
        if(r[0]=='1' and len(r)==1):
            ans+='1' #
            break
    return ans