from main.manager.storage_manager_utils import StorageManagerUtils
from main.model.thermos import Thermos


class StorageManager:
    def __init__(self, storage_list):
        self.storage_list = storage_list

    def add_storage(self, storage):
        self.storage_list.append(storage)

    def output_storages(self):
        print("Available storages:")
        print(*self.storage_list, sep="\n")

    def add_storages(self, storages):
        self.storage_list += storages

    @staticmethod
    def find_by_production_country(thermos_list, production_country):
        """
        >>> thermos_list = [Thermos(production_country="UK"), Thermos(production_country="UA"), Thermos(production_country="US"), Thermos(production_country="IT")]
        >>> found_thermoses = StorageManager.find_by_production_country(thermos_list, "UA")
        >>> found_thermoses[0].production_country
        'UA'
        """

        found_storages = []
        for storage in thermos_list:
            if storage.production_country == production_country:
                found_storages.append(storage)
        return found_storages

    @staticmethod
    def find_cheaper_than(thermos_list, price):
        """
        >>> thermos_list = [Thermos(price_in_uah=20), Thermos(price_in_uah=50), Thermos(price_in_uah=90), Thermos(price_in_uah=100)]
        >>> found_thermoses = StorageManager.find_cheaper_than(thermos_list, 60)
        >>> [thermos.price_in_uah for thermos in found_thermoses]
        [20, 50]
        """
        found_storages = []
        for storage in thermos_list:
            if storage.price_in_uah < price:
                found_storages.append(storage)
        return found_storages


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
