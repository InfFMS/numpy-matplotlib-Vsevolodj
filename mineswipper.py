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

fig, ax = plt.subplots()

data = np.array
print(data)
# Построение поля
plt.imshow(data, cmap='hot')

plt.xticks(range(8), labels=s)
plt.yticks(range(8), labels=[f"{i}" for i in range(8, 0, -1)])
plt.title("Шахматная доска")

circle = plt.Circle((x, y), 0.4, color= "red", label="ФЕРЗЬ")
ax.add_patch(circle)
