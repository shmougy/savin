# строка
sequence = "548976125489"

# пустой словарь
digit_count = {}

# перебираем каждую цифру в строке
for digit in sequence:
    # преобразуем цифру в int и проверяем наличие в словаре
    digit = int(digit)
    if digit in digit_count:
        # увеличиваем её счетчик на 1
        digit_count[digit] += 1
    else:
        # добавляем её с счетчиком 1
        digit_count[digit] = 1

print(digit_count)
