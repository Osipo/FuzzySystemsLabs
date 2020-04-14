from matplotlib import pyplot as plt
from collections import Counter
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10  # decile - Десятая часть числа, дециль.
histogram = Counter(decile(grade) for grade in grades)# dictionary  -> frequencies of grades

plt.bar([x-4 for x in histogram.keys()] # Сместить столбец влево на 4
            ,histogram.values()  #Высота столбца
            ,8) # Ширина каждого столбца = 8
plt.axis([-5,105,0,5]) # ось Х от 0 до 105, ось Y от 0 до 5
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Дециль")
plt.ylabel("Число студентов")
plt.title("Распределение оценок за экзамен")
plt.show()
# 2,3,5,7,11,13,17,19,23,27,29,31,37
#0000 0010 = 2
#0000 0011 = 3
#0000 0101 = 5
#0000 0111 = 7
#0000 1011 = 11 (3)   null -> 3 -> 5.
#0000 1101 = 13 (5)     5 -> 1.
#0001 0001 = 17 (1)   prev -> 7 -> prev
#0001 0011 = 19 (3)     1 -> 3 -> 7
#0001 0111 = 23 (7)     7 -> 3 -> 5 -> 7
#0001 1011 = 27 (3)
#0001 1101 = 29 (5)
#0001 1111 = 31 (7)
#0010 0101 = 37 (5)
#0010 1001 = 41 (1)
#0010 1011 = 43 (3)
#0010 1111 = 47 (7)