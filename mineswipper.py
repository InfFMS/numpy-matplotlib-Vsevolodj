# Задача:
# Создайте игровое поле для "Сапёра" размером 10×10.
# Поле должно быть представлено в виде двумерного массива.
# Разместите 15 мин случайным образом (обозначьте их числом −1).
# Для каждой клетки без мины подсчитайте количество мин в соседних клетках.
# Визуализируйте:
# Само поле (где мины выделены красным).
# Поле с числами, где указано количество мин вокруг каждой клетки (для наглядности).
import matplotlib.pyplot as plt
import numpy as np
import random
fig, ax = plt.subplots()
# Построение поля, значит идея такая: создаем массив, что будет суммой
# массивов 85 штук нулей и 15 штук (-1), а потом случайно их расставим в новый массив
data =[0]*85 + [-1]*15
t = 1
p =[]
o=1
while t<=100:
    x = random.randint(0,99)
    for i in p:
        if i == x:
            o =0
    if o !=0:
        p.append(x)
        t+=1
    o=1
t=0
index_nomber=0
minefield=[0]*100
for i in data:
    pon=p[index_nomber]
    t=data[index_nomber]
    minefield[pon]=t
    index_nomber=index_nomber+1
print(minefield)

# data = np.random.shuffle(data)
# print(data)

# plt.imshow(data, cmap='hot')
#
# plt.xticks(range(8), labels=s)
# plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
# plt.title("Шахматная доска")
#
# circle = plt.Circle((x, y), 0.4, color= "red", label="ФЕРЗЬ")
# ax.add_patch(circle)
