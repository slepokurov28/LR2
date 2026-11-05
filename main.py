from lab2 import DairyProduct, MeatProduct, Confectionery
import requests
from requests.models import PreparedRequest



def create_products():
    return [
        DairyProduct("Молоко 3.2%", 89.0, 58.0, fat_content=3.2),
        MeatProduct("Говядина", 450.0, 250.0, meat_type="говядина"),
        Confectionery("Торт шоколадный", 600.0, 420.0, sugar_content=35.0),
    ]



def input_number(prompt: str) -> float:
    while True:
        value = float(input(prompt))
        if value < 0:
            print("Значение не может быть отрицательным. Попробуйте снова.")
            continue
        return value



def product_menu(product):
    while True:
        print(f"Выбран продукт: {product.name}")
        print("Что вы хотите сделать?")
        print("  1. Показать характеристики экземпляра")
        print("  2. Рассчитать калорийность порции")
        print("  3. Рассчитать стоимость порции")
        print("  4. Проверить на высококалорийность")
        print("  0. Вернуться к выбору продукта")

        choice = input("Ваш выбор: ")

        if choice == "1":
            print("\n--- Характеристики ---")
            print(product)
            print(f"Категория: {product.get_category()}")

        elif choice == "2":
            grams = input_number("Введите вес порции в граммах: ")
            kcal = product.calculate_calories(grams)
            print(f"\nКалорийность порции {grams:.1f} г: {kcal:.1f} ккал")

        elif choice == "3":
            grams = input_number("Введите вес порции в граммах: ")
            price = product.calculate_price(grams)
            print(f"\nСтоимость порции {grams:.1f} г: {price:.2f} руб.")

        elif choice == "4":
            grams = input_number("Введите вес порции в граммах: ")
            if product.is_high_calorie(grams):
                print(f"\nПорция {grams:.1f} г высококалорийная (> 300 ккал).")
            else:
                print(f"\nПорция {grams:.1f} г НЕ высококалорийная (≤ 300 ккал).")

        elif choice == "0":
            return

        else:
            print("Неверный пункт меню.")
            continue

        input("\nНажмите Enter, чтобы вернуться в меню")


def main_menu(products):
    while True:
        print("Выбор продукта")
        for i, p in enumerate(products, start=1):
            print(f"  {i}. {p.name}  ({p.get_category()})")
        print("  0. Выйти из программы")

        choice = input("Ваш выбор: ")

        if choice == "0":
            return False

        if choice.isdigit() and 1 <= int(choice) <= len(products):
            product_menu(products[int(choice) - 1])
        else:
            print("Неверный пункт меню.")


def demo_external_packages():
    print("\n" + "=" * 60)
    print("Внешний пакет чере pip")
    print(f"Версия requests: {requests.__version__}")

    req = PreparedRequest()
    req.prepare_url("https://example.com/search", {"q": "python", "page": 1})
    print(f"ссылка: {req.url}")


def main():
    products = create_products()
    demo_external_packages()

    running = main_menu(products)

    if not running:
        print("\n. . .")


if __name__ == "__main__":
    main()