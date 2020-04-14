from collections import Counter
cities = [
    ([-122.3,47.53],"Единоросы"), #Координаты, значение.
    ([-96.85,32.85],"КПРФ"),
    ([-89.33,43.13],"ЛДПР")
]
x = ["a","b","b","a","c","d"]


def majority(labels):
    """All labels are sorted from the nearest to the furthest"""
    c = Counter(labels)
    # return most common element
    # it is tuple: (element, max_count)
    w, wc = c.most_common(1)[0]  # wc нужно для поиска совпадений.
    num_w = len([count
                 for count in c.values()
                 if count == wc])  # Число одинаковых по частоте элементов.

    if num_w == 1:  # Если нет совпадений, всё хорошо.
        return w
    else:
        return majority(labels[:-1])
c = Counter(x)
w, wc = c.most_common(1)[0]
n_w = len([cnt for cnt in c.values() if cnt == wc])
print(n_w)