import unittest
from main.manager.storage_manager import StorageManager
from main.manager.storage_manager_utils import StorageManagerUtils
from main.model.basket import Basket
from main.model.jar import Jar
from main.model.thermos import Thermos
from main.model.food_container import FoodContainer


def put_element_at_new_pos(place, given_list):
    return given_list[place]


class StorageManagerTest(unittest.TestCase):
    def setUp(self):
        self.first_storage = Basket(10, 500, 2, "Ukraine", "Black", "Z&Z", True)
        self.second_storage = Jar(1, 100, 0.3, "Germany", "Yellow", "Adolf & Co", "Jam jar")
        self.third_storage = Thermos(2.5, 200, 1.5, "China", "Pink", "Van Darkholm Storages", "Metal")
        self.fourth_storage = FoodContainer(5, 10000, 0.5, "Austria", "Green", "Kangaroo Container", "Oval")
        self.storage_list = [self.first_storage, self.second_storage, self.third_storage, self.fourth_storage]
        self.manager = StorageManager(self.storage_list)


class TestFinding(StorageManagerTest):
    # def test_finding_cheaper_then(self):
    #     self.assertEquals(first=self.manager.find_cheaper_than(110, self.storage_list), second=[self.second_storage])

    def test_finding_by_production_country(self):
        self.assertEqual(first=self.manager.find_by_production_country("China"), second=[self.third_storage])


if __name__ == '__main__':
    unittest.main()
