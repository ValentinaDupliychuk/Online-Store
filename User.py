from typing import Union
from Products import Basket
from Products import Products
from Products import Category


class User:
    """Класс User описывает пользователя книжного Интернет-магазина

    :param login: логин пользователя, используется для его аутенфикации
    :param password: пароль пользователя, используется для его аутенфикации
    :param item: объект класса Basket
    """

    def __init__(self, login: Union[str, int], password: Union[str, int], items_set_aside=None):
        self.__login = self.__check_login(login)
        self.__password = self.__check_password(password)

        self.item = Basket(items_set_aside)

    @staticmethod
    def __check_login(login):
        if not isinstance(login, (str, int)):
            raise TypeError("Логин должен быть представлен в виде строки или числа")
        return login

    @staticmethod
    def __check_password(password):
        password1 = input('Введите пароль еще раз для проверки: ')
        if password == password1:
            print("Пароли совпадают. Вы можете выбирать книги")
        else:
            raise ValueError("Пароли не совпадают. Введите пароль заново")
            return password

    @property
    def item(self) -> Basket:
        """
        Возвращает название книги, отложенной в Корзину
        :return: объект класса Basket
        """
        return self.item

    @item.setter
    def item(self, item: Basket) -> None:
        """
        Добавление новой книги в Корзину
        :param item: объект класса Basket
        """
        # if not isinstance(item, str):
        #     raise TypeError(f"Ожидается тип {str}, получен {type(item)}")
        self.item = item


if __name__ == '__main__':
    user1 = User(input("Введите Ваш логин: "), input('Введите пароль: '), "Маугли")

