from .food_product import FoodProduct

class DairyProduct(FoodProduct):

    def __init__(self, name, price_per_kg, calories_per_100g, fat_content: float):
        super().__init__(name, price_per_kg, calories_per_100g)
        self.__fat_content = None
        self.fat_content = fat_content

    @property
    def fat_content(self) -> float:
        return self.__fat_content

    @fat_content.setter
    def fat_content(self, value: float):
        if value < 0 or value > 100:
            raise ValueError("Жирность должна быть от 0 до 100%")
        self.__fat_content = value

    def get_category(self) -> str:
        return "Молочный продукт"

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, жирность: {self.fat_content}%"