from abc import ABC


class AbstractStorage(ABC):
    def __init__(self, capacity_in_liters, price_in_uah, weigth_in_kilograms, production_country, color, producer):
        self.capacity_in_liters = capacity_in_liters
        self.price_in_uah = price_in_uah
        self.weigth_in_kilograms = weigth_in_kilograms
        self.production_country = production_country
        self.color = color
        self.producer = producer

    def __str__(self):
        return "Capacity is: %s, Price is: %s, Weigth is: %s," \
               " Production country is: %s, Color is: %s, Producer is: %s" \
               % (self.capacity_in_liters, self.price_in_uah, self.weigth_in_kilograms, self.production_country, self.color, self.producer)
