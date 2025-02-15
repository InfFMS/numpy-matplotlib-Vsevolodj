# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt
import numpy as np
#введем с клавиатуры координаты ферзя
fig, ax = plt.subplots()
s = ["A","B","C","D","E","F","G","H"]
x = str(input("Введите заглавную букву:"))
y = int(input("Введите цифру:"))
# x = 5
# y = 5
y = 8-y
for i in range(0,8):
    if x == s[i]:
        x = i

data = np.array([[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]])
print(data)
# Построение поля
plt.imshow(data, cmap='hot')
# подпись осей
plt.xticks(range(8), labels=s)
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
plt.title("Шахматная доска")

for i in range(0,8,1):#горизонталь
    circle_1 = plt.Circle((i, y), 0.1, color="green")
    ax.add_patch(circle_1)
for i in range(0,8,1):#вертикаль
    circle_1 = plt.Circle((x, i), 0.1, color="green")
    ax.add_patch(circle_1)
for i in range(0,7,1):#лево верх
    if x-i< 0 or y-i <0:
        break
    circle_1 = plt.Circle((x-i,y-i), 0.1, color="green")
    ax.add_patch(circle_1)
for i in range(0,8,1):#право верх
    if i+ x > 7 or -(i - y) < 0:
        break
    circle_1 = plt.Circle((x+i,y -i), 0.1, color="green")
    ax.add_patch(circle_1)
for i in range(0,8,1):#лево низ
    if -(i- x) <0 or i + y > 7:
        break
    circle_1 = plt.Circle((x-i,y +i), 0.1, color="green")
    ax.add_patch(circle_1)
for i in range(0,8,1):#лево низ
    if x+i > 7 or i + y > 7:
        break
    circle_1 = plt.Circle((x+i,y +i), 0.1, color="green")
    ax.add_patch(circle_1)
#создали ферзя
circle = plt.Circle((x, y), 0.4, color= "red", label="ФЕРЗЬ")
ax.add_patch(circle)
plt.xlim(-5,10)
plt.ylim(15,-5)
plt.legend(loc=(1, 1))
plt.show()
