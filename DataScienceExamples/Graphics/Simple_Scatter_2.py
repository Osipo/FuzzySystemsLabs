from matplotlib import pyplot as plt
test_1_grades=[99,90,85,87,97,80]
test_2_grades=[100,85,60,90,70,80]
plt.scatter(test_1_grades,test_2_grades)
plt.title('Сопоставимые оси')
plt.xlabel('Оценки за Тест №1')
plt.ylabel('Оценки за Тест №2')
plt.axis('equal')
plt.show()