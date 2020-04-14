import mpmath
import random
from DataScienceExamples.FunctionalFun.Vectors import dot
from functools import reduce
from collections import Counter
def summa(x,y):
    return x+y
def sqr(x):
    return x*x

def med(data):
    l = len(data)
    if(l>=2):
        if(l&1!=0):
            k = (l)//2
            return data[k]
        else:
            k = l//2
        return (data[k-1]+data[k])//2

"""Возвращает значение в х, соответствующее p-ому проценту данных"""
def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

"""Возвращает значение, определяющее диапозон между 75% данных и 25% данных"""
def interquantile(x):
    return quantile(x,0.75) - quantile(x,0.25)


"""Возвращает список, так как мод может быть несколько."""
def moda(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return  [x_i for x_i, count in counts.items()
            if count == max_count
            ]
"""Среднее"""
def mean(x):
    return sum(x)/len(x)



"""Отклонения от средней"""
def deviasion(x): #de_mean
    m = mean(x)
    return list(map(lambda y: y-m,x))

"""Квадрат Стандартного Отклонения - Дисперсия"""
def variance(x):
    n = len(x)
    return reduce(summa,list(map(sqr,deviasion(x))))/(n-1)
def standard_deviation(x):
    return mpmath.sqrt(variance(x))
"""Коварианция. - Отклонения от средней двух величин x,y взятых вместе, как произведение dev(x*y) соответственно"""
def covariance(x,y):
    n = len(x)
    return dot(deviasion(x),deviasion(y))/(n-1)


"""Корреляция. """
def correlation(x,y):
    stddev_x = mpmath.sqrt(variance(x)) # Standard Deviasion - the root from variance
    stddev_y = mpmath.sqrt(variance(y))
    if stddev_x > 0 and stddev_y > 0:
        return covariance(x,y)/ stddev_x / stddev_y
    else:
        return 0 # Если переменные не меняются, то корреляция равна 0


"""Размах данных"""
def diaposon(x):
    return max(x) - min(x)

"""
# data = [4,4,4,5,5,3,3,3,3,3,5,4,4,2,2,2]
data = list(range(101)) # from 0 to 100 inclusive (101 - exclusive)
random.shuffle(data)
print('Length: %d'%len(data))
print(data)
print(data[50])
n = len(data)
mean_d =  mean(data) # or reduce(summa,data)/n
deviasions = deviasion(data) #or  list(map(lambda x: x - mean_d,data))
stddev = mpmath.sqrt(reduce(summa,list(map(sqr,deviasions)))/(n-1)) # 29.3001706479672
stddev2 = mpmath.sqrt(variance(data))
print('Mean : '+str(mean_d))
print('Standart deviasion : '+str(stddev))
print('Standart deviasion f: '+str(stddev2))
print('Median : %d'%med(data))
print('Moda : '+str(moda(data)))"""
# print('Range: %d'%diaposon(data))