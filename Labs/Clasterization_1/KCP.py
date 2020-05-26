from DataScienceExamples.Classes import Point
from matplotlib import pyplot as plt
import math
import random
import numpy as np

#KCP - Алгоритм Кратчайшего незамкнутого пути
# Применяется для графов.
# k = количество_кластеров.
# Находим пару точек с наименьшим расстоянием (весами)
# и соединяем их ребром.
# while p is not connected.
# Найти несоединённую точку, ближайшую к соединённой
# соединить эти точки ребром.
# end while.
# удалить k - 1 самых длинных рёбер  с их точками из выборки.
# repeat.
print('Initialization....')
l = [] # points to be clustered
cl = [] # list of clusters.
weights = [] # weights.
i = 0 # iterable variable.
x = 0; y = 100 # x,y - coords for points.
while i < 1000: # quantity = 1000
    l.append(Point.Point(random.randrange(x,y),random.randrange(x,y)))
    # plt.plot(l[i].getX(),l[i].getY(),color=l[i].getColor(),linewidth=2,lineheight=2,linestyle='-')
    i+=1;
k = 5 # quantity of clusters.
i = 0; j = 0
for pi in l:
    weights.append([])
    for pj in l:
        weights[i].append(random.randrange(x,y))

print('Start...')