import csv
import sys
import os
import matplotlib.pyplot as plt

# Шлях до файлу
file_path = 'Data.csv'

# Перевірка, чи існує файл
if not os.path.exists(file_path):
    print(f"Файл {file_path} не знайдено!")
    sys.exit()

# Читання CSV-файлу
data = {}
years = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Зчитуємо заголовок
    for row in reader:
        country = row[0]  # Назва країни
        values = row[4:14]  # Значення за 2014-2023 роки
        # Перетворюємо дані на числа, замінюємо відсутні значення (.. або '') на 0
        data[country] = [float(v) if v not in ['..', ''] else 0 for v in values]

# Імена країн
ukraine = 'Ukraine'
usa = 'United States'

# Перевіряємо, чи є дані для обраних країн
if ukraine not in data or usa not in data:
    print(f"Дані для України або США відсутні!")
    sys.exit()

# Вибираємо значення для України та США
ukraine_values = data[ukraine]
usa_values = data[usa]

# 2.1. Побудова лінійного графіка для двох країн
plt.figure(figsize=(10, 6))
plt.plot(years, ukraine_values, label='Ukraine', marker='o', color='blue')
plt.plot(years, usa_values, label='United States', marker='o', color='green')

# Додавання підписів
plt.xlabel('Year')
plt.ylabel('Children out of school, primary')
plt.title('Динаміка показника "Children out of school, primary" для України та США')
plt.legend()
plt.grid(True)
plt.show()
