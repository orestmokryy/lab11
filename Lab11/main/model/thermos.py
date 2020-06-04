from main.model.abstract_storage import AbstractStorage


class Thermos(AbstractStorage):
    def __init__(self, capacity_in_liters=0, price_in_uah=0, weigth_in_kilograms=0,
                 production_country=None, color=None, producer=None, body_material=None):
        super().__init__(capacity_in_liters, price_in_uah, weigth_in_kilograms, production_country, color, producer)
        self.body_material = body_material

    def __str__(self):
        return super().__str__() + ", Body is made of %s" % self.body_material
