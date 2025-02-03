# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
value =[0]*6
dice_rolls = np.random.randint(1,7,1000)
# print(dice_rolls)
for number in range(1,7):
    for i in range(0,1000):
        if number==dice_rolls[i]:
            value[number-1]+=1
print("Столько раз выпадало каждое значение:",value)
chance = [element/ 1000 for element in value]
print("Вероятность выпадения каждого значения:",chance)
max=0
count = 1
for i in range(0, 1000-1):
    if (dice_rolls[i] == dice_rolls[i+1]):
        count+= 1
    else:
        if max < count:
            max = count
        count = 0
print(max)
categories = ["1", "2", "3", "4", "5", "6"]
plt.bar(categories, value, color='green')
plt.title("Столбчатая диаграмма")
ax.set_xlabel("Выпавшее число", fontsize=10, color='black', labelpad=0)    # +
ax.set_ylabel("Количество выпадений", fontsize=10, color='black', labelpad=0)  # +
plt.show()