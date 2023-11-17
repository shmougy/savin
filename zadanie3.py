# список
my_list = [3, 7, -2, 0, 8, -4, 5, 0, 10, -1]

# сумма пол. элементов списка
positive_sum = sum(x for x in my_list if x > 0)

# ищем индекс первого 0 элемента
first_zero_index = next((i for i, x in enumerate(my_list) if x == 0), None)

#  считаем сумму элементов после 0-элемента
if first_zero_index is not None:
    sum_after_zero = sum(my_list[first_zero_index + 1:])
else:
    sum_after_zero = "Сумму посчитать нельзя"

# удаляем все отрицательные
my_list = [x for x in my_list if x >= 0]

print(f"Сумма положительных элементов списка: {positive_sum}")
print(f"Сумма элементов списка после первого нуля: {sum_after_zero}")
print(f"Список без отрицательных элементов: {my_list}")
