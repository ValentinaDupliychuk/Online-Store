from typing import Union
import random


class Products:
    """
    Класс, описывающий товары, которые есть в наличии.

    :param name: название книги. Данный аргумент является приватным и не изменяется
    :param rating: рейтинг той или иной книги, имеет значение от 0 до 10.
    Данный аргумент является публичным и может быть изменен пользователями
    :param price: стоимость книги. Данный аргумент является защищенным
    """
    def __init__(self, name: str, rating: Union[int, float], price: Union[int, float]):
        self.__name = self.__check_name(name)
        self.rating = self.check_rating(rating)
        self._price = self._check_price(price)
        self.change_rating(rating)

    @staticmethod
    def __check_name(name):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть в формате строки")
        return name

    @staticmethod
    def check_rating(rating):
        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен иметь численное значение")
        if rating <= 0 or rating > 10:
            raise ValueError("Рейтинг рассчитывается от 0 до 10")
        return rating

    @staticmethod
    def _check_price(price):
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должен иметь численное значение")
        if price < 0:
            raise ValueError("Цена рассчитывается от 0 до 10")
        return price

    def change_rating(self, rating):
        """Функция для изменения значения рейтинга"""
        while rating <= 0 or rating > 10:
            rating += random.random()
            return rating

    def __repr__(self) -> str:
        return f"Products({self.__name}, {self.rating}, {self._price})"

    def __str__(self) -> str:
        return f"Наименование товара: {self.__check_name(self.__name)}, рейтинг: {self.check_rating(self.rating)}, " \
               f"цена: {self._check_price(self._price)}, "


class Category(Products):
    """Класс с категориями книг, представленными в магазине.

    Атрибут класса представлен в виде словаря:
    ключ - название категории, значение - количество произведений, относящихся к данной категории.
    Значение количества произведений может использоваться в дальнейшем для добавления новых произведений в категории"""

    CAT = {
        "Зарубежная классическая литература": 166472,    # Данные взяты с сайта https://www.livelib.ru/genres
        "Русская классическая литература": 127580,
        "Детские книги": 176646,
        "Детективы": 64640,
        "Фэнтези": 32437,
        "Фантастика": 63065,
        "Современная проза": 103219,
        "Приключения": 54138,
        "Ужасы": 32629
    }

    def __init__(self, category_name: str, name=None, rating=None, price=None):
        super().__init__(name=name, rating=rating, price=price)
        self.category_name = category_name

    @property
    def cat_name(self):
        return self.category_name

    @cat_name.setter
    def cat_name(self, category_name: str):
        if not isinstance(category_name, str):
            raise TypeError('Категория задается строковым значением')
        if not (category_name in self.CAT):
            raise ValueError('Данная категория отсутствует')

    def __str__(self):
        return f"Книга относится к категории {self.category_name}."


class Basket(Products):
    """В данном классе содержится массив купленных товаров

    :param items_set_aside:наименования товара, отложенные в Корзину
    :param counter: количество отложенных книг
    """

    counter = 0

    def __init__(self, items_set_aside: str, name=None, rating=None, price=None):
        super().__init__(name=name, rating=rating, price=price)
        self.items_set_aside = self.check_items_set_aside(items_set_aside)


    def __new__(cls, *args):
        cls.append_counter()
        print(f"Добавлено {cls.counter} книга в {cls.__name__}")
        return super().__new__(cls)


    @classmethod
    def append_counter(cls):
        """Метод, привязанный к классу Basket. Инициирует счетчик количества отложенных книг"""
        cls.counter += 1

    @staticmethod
    def check_items_set_aside(items_set_aside: str):
        """Функция проверяет, имеет ли значение параметра items_set_aside строковое значение"""
        if not isinstance(items_set_aside, str):
            raise TypeError("Книги, отложенные в Корзину должны быть представлены в виде строки")
        return items_set_aside

    def __str__(self):
        return f"Книга {self.check_items_set_aside(self.items_set_aside)} отложена в Корзину"


if __name__ == '__main__':
    item1 = Products("Маугли", 9, 200)
    print(item1)

    item1 = Category("Детская литература", "книга", 9, 200)

    print(item1)

    item1 = Basket("Маугли", "Маугли", 9, 200)


    print(item1)