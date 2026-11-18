from lab2 import DairyProduct, MeatProduct, Confectionery
from colorama import Fore, Style, init

init(autoreset=True)


def create_products():
    return [
        DairyProduct("Молоко 3.2%", 89.0, 58.0, fat_content=3.2),
        MeatProduct("Говядина", 450.0, 250.0, meat_type="говядина"),
        Confectionery("Торт шоколадный", 600.0, 420.0, sugar_content=35.0),
    ]


def input_number(prompt: str):
    while True:
        value = float(input(prompt))
        if value < 0:
            print(Fore.RED + "Значение не может быть отрицательным. Попробуйте снова." + Style.RESET_ALL)
            continue
        return value


def product_menu(product):
    while True:
        print("\n" + Fore.CYAN + "=" * 60 + Style.RESET_ALL)
        print(f"Выбран продукт: {Fore.YELLOW}{product.name}{Style.RESET_ALL}")
        print("Что вы хотите сделать?")
        print("  1. Показать характеристики экземпляра")
        print("  2. Рассчитать калорийность порции")
        print("  3. Рассчитать стоимость порции")
        print("  4. Проверить на высококалорийность")
        print("  0. Вернуться к выбору продукта")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            print("\n Характеристики ")
            print(product)


        elif choice == "2":
            grams = input_number("Введите вес порции в граммах: ")
            kcal = product.calculate_calories(grams)
            print(f"\nКалорийность порции {grams:.1f} г: "
                  f"{Fore.GREEN}{kcal:.1f} ккал{Style.RESET_ALL}")

        elif choice == "3":
            grams = input_number("Введите вес порции в граммах: ")
            price = product.calculate_price(grams)
            print(f"\nСтоимость порции {grams:.1f} г: "
                  f"{Fore.GREEN}{price:.2f} руб.{Style.RESET_ALL}")

        elif choice == "4":
            grams = input_number("Введите вес порции в граммах: ")
            if product.is_high_calorie(grams):
                print(Fore.RED + f"\nПорция {grams:.1f} г ВЫСОКОКАЛОРИЙНАЯ (> 300 ккал)." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"\nПорция {grams:.1f} г не является высококалорийной (≤ 300 ккал)." + Style.RESET_ALL)

        elif choice == "0":
            return

        else:
            print(Fore.RED + "Неверный пункт меню." + Style.RESET_ALL)
            continue

        input(Fore.MAGENTA + "\nНажмите Enter, чтобы вернуться в меню..." + Style.RESET_ALL)


def main_menu(products):
    while True:
        print(Fore.CYAN + "ГЛАВНОЕ МЕНЮ — ВЫБОР ПРОДУКТА" + Style.RESET_ALL)
        for i, p in enumerate(products, start=1):
            print(f"  {i}. {p.name}  ({p.get_category()})")
        print("  0. Выйти из программы")

        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            return False

        if choice.isdigit() and 1 <= int(choice) <= len(products):
            product_menu(products[int(choice) - 1])
        else:
            print(Fore.RED + "Неверный пункт меню." + Style.RESET_ALL)


def demo_external_packages():
    print(Fore.GREEN + "..." + Style.RESET_ALL)


def main():
    products = create_products()
    demo_external_packages()

    running = main_menu(products)

    if not running:
        print(Fore.CYAN + "\nДо свидания!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()