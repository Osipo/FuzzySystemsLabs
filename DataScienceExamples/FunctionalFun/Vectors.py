from functools import reduce
import math
def vector_add(v,w):
    return[v_i+w_i for v_i, w_i in zip(v,w)]

def vector_sub(v,w):
    return[v_i-w_i for v_i,w_i in zip(v,w)]

"""Покомпонентная сумма значений векторов. Сумма по столбцам."""
def vector_sum(vectors):
    return reduce(vector_add,vectors) #sum of vectors>=2

def vector_scalar_mul(c,v):
    """c - число, v - вектор"""
    return [c*v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    """Вычислить вектор, чей i-элемент равен среднему значению всех i-элементов входящих векторов."""
    return vector_scalar_mul(1/n,vector_sum(vectors))

"""Скалярное произведение двух векторов"""
def dot(v,w):
    """Это сумма их покомпонентых произведений т.е. v_1*w_1 + v_2*w_2+...+v_n*w_n"""
    return sum(v_i*w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    return sum_of_squares(vector_sub(v,w)) #(x1-y1)*(x1-y1)+(x2-y2)*(x2-y2)

def distance(v,w):
    return magnitude(vector_sub(v,w)) # root: (x1-y1)*(x1-y1)+(x2-y2)*(x2-y2)+...+(xn-yn)*(xn-yn)

#Relation between increment of function and increment of argument.
def difference_quotient(f,x,h):
    return (f(x + h) - f(x)) / h

#Relation between increment of function and increment of i-argument of vector.
def partial_difference_quotient(f,v,i,h):
    w = [v_j +(h if j==i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h

def estimate_gradient(f,v,h=0.00001):
    return [partial_difference_quotient(f,v,i,h) for i, _ in enumerate(v)]

def stepForGradient(v,gradient,step_size):
    return [v_i+step_size*gradient_i for v_i,gradient_i in zip(v,gradient)]


#Количество строк и столбцов в матрице А.
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A,i):
    return A[i] # i-ая строка матрицы A
def get_column(A,j):
    return [A_i[j] for A_i in A] # j-ый столбец матрицы А.

"""Создаёт матрицу размером num_rows * num_columns где элемент i-ой строки j-ого столбца
равен результату функции entry_fn(i,j)
"""
def make_matrix(num_rows,num_columns,entry_fn):
    return  [[entry_fn(i,j)
             for j in range(num_columns)]
             for i in range(num_rows)
            ]
"""Функция, генерирующая единичные элементы матрицы"""
def is_diagonal(i,j):
    return 1 if i==j else 0


# a = [1,2]
# b = [2,1]
# c = vector_add(a,b)
# d = vector_sum([a,b,c])
# d = sum_of_squares(d)
# print(d)