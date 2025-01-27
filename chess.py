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
y = 8-y
for i in range(0,8):
    if x == s[i]:
        x = i

data = np.array([[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]])
print(data)
# Построение поля
plt.imshow(data, cmap='hot')

plt.xticks(range(8), labels=s)
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
plt.title("Шахматная доска")

circle = plt.Circle((x, y), 0.4, color= "red", label="ФЕРЗЬ")
ax.add_patch(circle)

circle_1 = plt.Circle((x+1, y), 0.1, color= "green")
ax.add_patch(circle_1)
circle_2 = plt.Circle((x+2, y), 0.1, color= "green")
ax.add_patch(circle_2)
circle_3 = plt.Circle((x+3, y), 0.1, color= "green")
ax.add_patch(circle_3)
circle_4 = plt.Circle((x+4, y), 0.1, color= "green")
ax.add_patch(circle_4)
circle_5 = plt.Circle((x+5, y), 0.1, color= "green")
ax.add_patch(circle_5)
circle_6 = plt.Circle((x+6, y), 0.1, color= "green")
ax.add_patch(circle_6)
circle_7 = plt.Circle((x+7, y), 0.1, color= "green")
ax.add_patch(circle_7)
circle_an1 = plt.Circle((x-1, y), 0.1, color= "green")
ax.add_patch(circle_an1)
circle_an2 = plt.Circle((x-2, y), 0.1, color= "green")
ax.add_patch(circle_an2)
circle_an3 = plt.Circle((x-3, y), 0.1, color= "green")
ax.add_patch(circle_an3)
circle_an4 = plt.Circle((x-4, y), 0.1, color= "green")
ax.add_patch(circle_an4)
circle_an5 = plt.Circle((x-5, y), 0.1, color= "green")
ax.add_patch(circle_an5)
circle_an6 = plt.Circle((x-6, y), 0.1, color= "green")
ax.add_patch(circle_an6)
circle_an7 = plt.Circle((x-7, y), 0.1, color= "green")
ax.add_patch(circle_an7)

circle_1y = plt.Circle((x, y+1), 0.1, color= "green")
ax.add_patch(circle_1y)
circle_2y = plt.Circle((x, y+2), 0.1, color= "green")
ax.add_patch(circle_2y)
circle_3y = plt.Circle((x, y+3), 0.1, color= "green")
ax.add_patch(circle_3y)
circle_4y = plt.Circle((x, y+4), 0.1, color= "green")
ax.add_patch(circle_4y)
circle_5y = plt.Circle((x, y+5), 0.1, color= "green")
ax.add_patch(circle_5y)
circle_6y = plt.Circle((x, y+6), 0.1, color= "green")
ax.add_patch(circle_6y)
circle_7y = plt.Circle((x, y+7), 0.1, color= "green")
ax.add_patch(circle_7y)
circle_an1y = plt.Circle((x, y-1), 0.1, color= "green")
ax.add_patch(circle_an1y)
circle_an2y = plt.Circle((x, y-2), 0.1, color= "green")
ax.add_patch(circle_an2y)
circle_an3y = plt.Circle((x, y-3), 0.1, color= "green")
ax.add_patch(circle_an3y)
circle_an4y = plt.Circle((x, y-4), 0.1, color= "green")
ax.add_patch(circle_an4y)
circle_an5y = plt.Circle((x, y-5), 0.1, color= "green")
ax.add_patch(circle_an5y)
circle_an6y = plt.Circle((x, y-6), 0.1, color= "green")
ax.add_patch(circle_an6y)
circle_an7y = plt.Circle((x, y-7), 0.1, color= "green")
ax.add_patch(circle_an7y)

# ---------------------------------------------------------


circle_1d = plt.Circle((x+1, y+1), 0.1, color= "green")
ax.add_patch(circle_1d)
circle_2d = plt.Circle((x+2, y+2), 0.1, color= "green")
ax.add_patch(circle_2d)
circle_3d = plt.Circle((x+3, y+3), 0.1, color= "green")
ax.add_patch(circle_3d)
circle_4d = plt.Circle((x+4, y+4), 0.1, color= "green")
ax.add_patch(circle_4d)
circle_5d = plt.Circle((x+5, y+5), 0.1, color= "green")
ax.add_patch(circle_5d)
circle_6d = plt.Circle((x+6, y+6), 0.1, color= "green")
ax.add_patch(circle_6d)
circle_7d = plt.Circle((x+7, y+7), 0.1, color= "green")
ax.add_patch(circle_7d)
circle_an1d = plt.Circle((x-1, y-1), 0.1, color= "green")
ax.add_patch(circle_an1d)
circle_an2d = plt.Circle((x-2, y-2), 0.1, color= "green")
ax.add_patch(circle_an2d)
circle_an3d = plt.Circle((x-3, y-3), 0.1, color= "green")
ax.add_patch(circle_an3d)
circle_an4d = plt.Circle((x-4, y-4), 0.1, color= "green")
ax.add_patch(circle_an4d)
circle_an5d = plt.Circle((x-5, y-5), 0.1, color= "green")
ax.add_patch(circle_an5d)
circle_an6d = plt.Circle((x-6, y-6), 0.1, color= "green")
ax.add_patch(circle_an6d)
circle_an7d = plt.Circle((x-7, y-7), 0.1, color= "green")
ax.add_patch(circle_an7d)
# --
circle_1yd = plt.Circle((x-1, y+1), 0.1, color= "green")
ax.add_patch(circle_1yd)
circle_2yd = plt.Circle((x-2, y+2), 0.1, color= "green")
ax.add_patch(circle_2yd)
circle_3yd = plt.Circle((x-3, y+3), 0.1, color= "green")
ax.add_patch(circle_3yd)
circle_4yd = plt.Circle((x-4, y+4), 0.1, color= "green")
ax.add_patch(circle_4yd)
circle_5yd = plt.Circle((x-5, y+5), 0.1, color= "green")
ax.add_patch(circle_5yd)
circle_6yd = plt.Circle((x-6, y+6), 0.1, color= "green")
ax.add_patch(circle_6yd)
circle_7yd = plt.Circle((x-7, y+7), 0.1, color= "green")
ax.add_patch(circle_7yd)
circle_an1yd = plt.Circle((x+1, y-1), 0.1, color= "green")
ax.add_patch(circle_an1yd)
circle_an2yd = plt.Circle((x+2, y-2), 0.1, color= "green")
ax.add_patch(circle_an2yd)
circle_an3yd = plt.Circle((x+3, y-3), 0.1, color= "green")
ax.add_patch(circle_an3yd)
circle_an4yd = plt.Circle((x+4, y-4), 0.1, color= "green")
ax.add_patch(circle_an4yd)
circle_an5yd = plt.Circle((x+5, y-5), 0.1, color= "green")
ax.add_patch(circle_an5yd)
circle_an6yd = plt.Circle((x+6, y-6), 0.1, color= "green")
ax.add_patch(circle_an6yd)
circle_an7yd = plt.Circle((x+7, y-7), 0.1, color= "green")
ax.add_patch(circle_an7yd)




# ax.set_xlim(0, 1)
# ax.set_ylim(0, 1)
plt.legend(loc=(1, 1))




plt.show()
