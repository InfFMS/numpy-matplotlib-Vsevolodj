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
# print(minefield)
line_minefield = minefield
minefield = np.array(minefield)
minefield =minefield.reshape((10,10))
print(minefield)
plt.imshow(minefield, cmap='Set1')
plt.title("Mineswipper")

ax.text(0, 0, '1', color ="orange", horizontalalignment='center', verticalalignment='center', size = 20)

ax.text(9, 9, '1', color ="orange", horizontalalignment='center', verticalalignment='center', size = 20)

for i in range(10,89):
    if not(i%10==0 or i%10==9):
        count = 0
        count = minefield[i%10+1,i//10]+line_minefield[i-10-1]+line_minefield[i-10+1]+line_minefield[i-1]+line_minefield[i+1]+line_minefield[i+10]+line_minefield[i+10-1]+line_minefield[i+10+1]
        ax.text(i%10, i//10, count*-1, color="orange", horizontalalignment='center', verticalalignment='center', size=20)
ax.set_axis_off()
# plt.xlim(0,5)
# plt.ylim(15,-5)
plt.legend(loc=(1, 1))
plt.show()
