from .food_product import FoodProduct

class MeatProduct(FoodProduct):
    """Мясной продукт."""

    def __init__(self, name, price_per_kg, calories_per_100g, meat_type: str):
        super().__init__(name, price_per_kg, calories_per_100g)
        self.__meat_type = None
        self.meat_type = meat_type

    @property
    def meat_type(self) -> str:
        return self.__meat_type

    @meat_type.setter
    def meat_type(self, value: str):
        if not value:
            raise ValueError("Тип мяса не может быть пустым")
        self.__meat_type = value

    def get_category(self) -> str:
        return "Мясной продукт"

    # Переопределение метода родителя (требование задания)
    def calculate_calories(self, portion_grams: float) -> float:
        """Для мясных продуктов учитываем 10% потерь при готовке."""
        base = super().calculate_calories(portion_grams)
        return base * 0.9

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, тип мяса: {self.meat_type}"