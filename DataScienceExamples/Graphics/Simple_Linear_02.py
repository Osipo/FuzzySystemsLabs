from matplotlib import pyplot as plt
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = list([x+y for x,y in zip(variance,bias_squared)])
xs = list([i for i, _ in enumerate(variance)])
plt.plot(xs,variance,'g-',label='Дисперсия')
plt.plot(xs,bias_squared, 'r-.',label='Смещение Х^2')
plt.plot(xs,total_error, 'b:',label='Суммарная ошибка')
# Если для каждой линии задана метка, то легенда может отображаться автоматически.
plt.legend(loc=9) # Наверху посередине
plt.xlabel('Сложность модели')
plt.title('Компромисс между смещением и дисперсией')
plt.show()