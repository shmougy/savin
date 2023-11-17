def is_digits_in_descending_order(number):
    last_digit = 9

    while number > 0:
        digit = number % 10
        if digit > last_digit:
            return False
        last_digit = digit
        number //= 10

    return True


while True:
    try:
        num = int(input("Введите натуральное число (введите 0 для выхода): "))

        if num == 0:
            print("Выход из программы.")
            break

        if num > 0 and is_digits_in_descending_order(num):
            print("Последовательность цифр упорядочена по убыванию.")
        else:
            print("Введите положительное натуральное число.")

    except ValueError:
        print("Ошибка: Введите корректное натуральное число.")
