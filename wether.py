# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import random
import matplotlib.pyplot as plt
fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # 1 ряд, 2 столбца
warm_days=0
average_temp =0

days_in_year = 365
temp= [random.randint(-10, 30) for i in range(days_in_year)]
# print(f"Дневная температура: {temp}")
for i in range(len(temp)):
    if temp[i]>25:
        warm_days+=1
    average_temp+=temp[i]
average_temp=average_temp/days_in_year

max=0
count = 1
for i in range(0, days_in_year-1):
    if (temp[i]<0 and temp[i+1]<0):
        count+= 1
    else:
        if max < count:
            max = count
        count = 0
print("Средняя температура:",average_temp)
print("Дней с температурой больше 25°C:", warm_days)
print("Cамая длинная последовательность, когда температура была ниже 0°C:",max)
number_days = list(range(1,days_in_year+1))
axs[0].plot(number_days, [0]*days_in_year, color="black")
for i in range(days_in_year):
    if temp[i]<=0:
        axs[0].scatter(number_days[i], temp[i], label="Temp", color="blue")
    else:
        axs[0].scatter(number_days[i], temp[i], label="Temp", color="orange")
axs[0].plot(number_days , temp, label="Temp", color="grey")
axs[0].set_title("Temperature")
axs[0].set_xlabel("Days", fontsize=10, color='black', labelpad=0)
axs[0].set_ylabel("Temperature, °C", fontsize=10, color='black', labelpad=0)
one = two = tree = four = 0
for i in range(days_in_year):
    if temp[i]<0:
        one +=1
    elif temp[i] < 10:
        two += 1
    elif temp[i] < 20:
        tree += 1
    elif temp[i] < 30:
        four += 1


axs[1].bar(["-10 - 0", "0 - 10","10 - 20","20 - 30"] , [one,two,tree,four], label="Temp", color="grey")
axs[1].set_title("Distribution temperature")
axs[1].set_ylabel("Quantity days", fontsize=10, color='black', labelpad=0)
axs[1].set_xlabel("Temperature, °C", fontsize=10, color='black', labelpad=0)
text_stats = (f'54345')
plt.text(-2,100,f'Средняя температура:{round(average_temp)}°C\nДней с температурой больше 25°C: {warm_days} дней\n'
                f'Cамая длинная последовательность, \nкогда температура была ниже 0°C: {max} days')
plt.subplots_adjust( top=0.5)
plt.show()