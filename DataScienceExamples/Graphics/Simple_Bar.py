from matplotlib import pyplot as plt
movies=["Endy Hall","Ben Gur","Kasablanka","Gandy","Westside History"]
num_oscars = [5,11,3,8,10]
xs = [i + 0.1 for i ,_ in enumerate(movies)]
plt.bar(xs,num_oscars)
plt.ylabel("Количество наград")
plt.title("Любимые фильмы")
#Добавить метки на оси Х с названиями фильмов в центре кажлого интервала.
plt.xticks([i + 0.5 for i, _ in enumerate(movies)],movies)
plt.show()