from main.model.thermos import Thermos


class StorageManagerUtils:

    @staticmethod
    def sort_by_capacity(given_list, sort_type=False):
        """
        >>> thermos_list = [Thermos(2), Thermos(1), Thermos(5), Thermos(10)]
        >>> StorageManagerUtils.sort_by_capacity(thermos_list)
        >>> [thermos.capacity_in_liters for thermos in thermos_list]
        [1, 2, 5, 10]
        """
        given_list.sort(key=lambda storage: storage.capacity_in_liters, reverse=sort_type)

    @staticmethod
    def sort_by_color(given_list, sort_type=False):
        """
        >>> thermos_list = [Thermos(color="Blue"), Thermos(color="White"), Thermos(color="Pink"), Thermos(color="A")]
        >>> StorageManagerUtils.sort_by_color(thermos_list)
        >>> [thermos.color for thermos in thermos_list]
        ['A', 'Blue', 'Pink', 'White']
        """
        given_list.sort(key=lambda storage: storage.color, reverse=sort_type)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
