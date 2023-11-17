
menu = {
    "торт": ["шоколадный торт", 200, 10],
    "пирожное": ["ванильное пирожное", 50, 20],
    "маффин": ["шоколадный маффин", 80, 15],
    "пончик": ["классический пончик", 60, 25],
    "печенье": ["шоколадное печенье", 40, 30],
    "эклер": ["крем-эклер", 70, 12],
}

# вывод описания продукции
def view_description():
    for key, value in menu.items():
        print(f"{key} - {value[0]}")

# вывод цен продукции
def view_price():
    for key, value in menu.items():
        print(f"{key} - {value[1]} рублей за 100 грамм")

# вывод количества продукции
def view_quantity():
    for key, value in menu.items():
        print(f"{key} - {value[2]} грамм")

# вывод всей информации
def view_all_info():
    for key, value in menu.items():
        print(f"{key} - {value[0]}, Цена: {value[1]} рублей за 100 грамм, Количество: {value[2]} грамм")

# совершение покупки
def buy_product():
    total_cost = 0
    while True:
        print("Введите название продукции (или 'n' для завершения покупки): ")
        product_name = input()
        if product_name == 'n':
            break
        elif product_name in menu:
            print(f"Введите количество {product_name}: ")
            try:
                quantity = int(input())
                if quantity <= menu[product_name][2]:
                    total_cost += (quantity * menu[product_name][1]) / 100
                    menu[product_name][2] -= quantity
                    print(f"Добавлено {quantity} грамм {product_name} в корзину.")
                else:
                    print(f"Извините, недостаточно {product_name} в наличии.")
            except ValueError:
                print("Пожалуйста, введите корректное количество.")
        else:
            print("Извините, продукции с таким названием нет в меню.")
    print(f"Общая стоимость покупки: {total_cost} рублей")

# цикл программы
while True:
    print("\nМеню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        view_description()
    elif choice == "2":
        view_price()
    elif choice == "3":
        view_quantity()
    elif choice == "4":
        view_all_info()
    elif choice == "5":
        buy_product()
    elif choice == "6":
        print("До свидания!")
        break
    else:
        print("Пожалуйста, выберите правильный пункт меню.")
1