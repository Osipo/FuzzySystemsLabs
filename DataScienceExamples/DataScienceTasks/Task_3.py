from collections import Counter
from DataScienceExamples.FunctionalFun.Vectors import distance
from matplotlib import pyplot as plt

#Считает наиболее встречаемый элемент label в данных (x,y,label)
def majority(labels):
    """All labels are sorted from the nearest to the furthest"""
    c = Counter(labels)
    #return most common element
    #it is tuple: (element, max_count)
    w, wc = c.most_common(1)[0] #wc нужно для поиска совпадений.
    num_w = len([count
                 for count in c.values()
                 if count == wc])# Число одинаковых по частоте элементов.
                 
    if num_w == 1: #Если нет совпадений, всё хорошо.
        return w
    else:
        return majority(labels[:-1]) #Иначе отбросить последнее значение, и посчитать снова.
def toCoords(p):
    return p[0]
def K_nearest_neighbours(k,labeled_points,np):
    """"Each labeled_point is tuple: (point,label)"""
    by_distance = sorted(labeled_points, key=lambda p:distance(toCoords(p),np)) #distance - декартовое расстояние.
    k_nearest_labels = [label for _, label in by_distance[:k]] #Получить значения k ближайших точек.
    return majority(k_nearest_labels) # найти большинство голосов по ним.

#data.
cities = [
    ([-122.3,47.53],"Единоросы"), #Координаты, значение.
    ([-96.85,32.85],"КПРФ"),
    ([-89.33,43.13],"ЛДПР")
]

#select optimal K.
for k in [1,3,5,7]:
    num_c = 0

    #Для каждого элемента из данных, отсортировать остальные точки по расстоянию от ближайших до дальних к текущему элементу.
    #И выбрать k из них.
    #И посчитать по ним.
    for city in cities:
        coords, label = city
        other_cities = [other_city for other_city in cities if other_city != city]
        predicted_lang = K_nearest_neighbours(k,other_cities,coords)
        if predicted_lang == label:
            num_c += 1
    print(k,"(сосед(а,ей):",num_c,"correct from ",len(cities))