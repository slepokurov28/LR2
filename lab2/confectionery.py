from .food_product import FoodProduct

class Confectionery(FoodProduct):
    """Кондитерское изделие."""

    def __init__(self, name, price_per_kg, calories_per_100g, sugar_content: float):
        super().__init__(name, price_per_kg, calories_per_100g)
        self.__sugar_content = None
        self.sugar_content = sugar_content

    @property
    def sugar_content(self) -> float:
        return self.__sugar_content

    @sugar_content.setter
    def sugar_content(self, value: float):
        if value < 0 or value > 100:
            raise ValueError("Содержание сахара должно быть от 0 до 100%")
        self.__sugar_content = value

    def get_category(self) -> str:
        return "Кондитерское изделие"

    # Этот класс НЕ переопределяет calculate_calories (требование: один наследник переопределяет, другой — нет)

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, сахар: {self.sugar_content}%"