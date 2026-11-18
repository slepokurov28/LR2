from abc import ABC, abstractmethod

class FoodProduct(ABC):

    def __init__(self, name: str, price_per_kg: float, calories_per_100g: float):
        self.__name = None
        self.__price_per_kg = None
        self.__calories_per_100g = None
        self.name = name
        self.price_per_kg = price_per_kg
        self.calories_per_100g = calories_per_100g

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or not isinstance(value, str):
            raise ValueError("Название должно быть непустой строкой")
        self.__name = value

    @property
    def price_per_kg(self):
        return self.__price_per_kg

    @price_per_kg.setter
    def price_per_kg(self, value: float):
        if value <= 0:
            raise ValueError("Цена за кг должна быть положительной")
        self.__price_per_kg = value

    @property
    def calories_per_100g(self):
        return self.__calories_per_100g

    @calories_per_100g.setter
    def calories_per_100g(self, value: float):
        if value < 0:
            raise ValueError("Калорийность не может быть отрицательной")
        self.__calories_per_100g = value

    @abstractmethod
    def get_category(self):
        pass

    def calculate_calories(self, portion_grams: float):
        return (self.calories_per_100g * portion_grams) / 100.0

    def calculate_price(self, portion_grams: float):
        return (self.price_per_kg * portion_grams) / 1000.0

    def is_high_calorie(self, portion_grams: float):
        return self.calculate_calories(portion_grams) > 300

    def __str__(self):
        return (f"[{self.get_category()}] {self.name}, "
                f"цена: {self.price_per_kg:.2f} руб/кг, "
                f"калорийность: {self.calories_per_100g:.1f} ккал/100г")