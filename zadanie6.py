# кортеж чисел
my_tuple = (5, -2, 7, -1, 0, 3, 8, -4, 5)

# счетчик положительных элементов
positive_count = 0

# перебор элементов кортежа + счетчик
for number in my_tuple:
    if number > 0:
        positive_count += 1

# результат
print(f"Количество положительных элементов: {positive_count}")
