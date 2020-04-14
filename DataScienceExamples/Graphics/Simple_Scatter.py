from matplotlib import pyplot as plt
friends = [70,65,72,73,66,55,56,71,50,62]
minutes =[175,170,205,200,120,130,220,105,145,190]
labels =['a','b','c','d','e','f','g','h','i','j']
plt.scatter(friends,minutes)
for label, friend_c, minute_c in zip(labels,friends,minutes):
    plt.annotate(label,xy=(friend_c,minute_c),xytext=(5,-5),textcoords='offset points')
plt.title('Зависимость между количеством друзей и минут')
plt.xlabel('Число друзей')
plt.ylabel('Время в минутах')
plt.show()