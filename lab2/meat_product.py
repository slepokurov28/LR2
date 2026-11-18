from .food_product import FoodProduct

class MeatProduct(FoodProduct):

    def __init__(self, name, price_per_kg, calories_per_100g, meat_type: str):
        super().__init__(name, price_per_kg, calories_per_100g)
        self.__meat_type = None
        self.meat_type = meat_type

    @property
    def meat_type(self):
        return self.__meat_type

    @meat_type.setter
    def meat_type(self, value: str):
        if not value:
            raise ValueError("Тип мяса не может быть пустым")
        self.__meat_type = value

    def get_category(self):
        return "Мясной продукт"

    def calculate_calories(self, portion_grams: float):
        base = super().calculate_calories(portion_grams)
        return base * 0.9

    def __str__(self):
        base = super().__str__()
        return f"{base}, тип мяса: {self.meat_type}"