from typing import Union


class Products:
    """
    Класс, описывающий товары, которые есть в наличии.

    :param name: название книги. Данный аргумент является приватным и не изменяется
    :param rating: рейтинг той или иной книги, имеет значение от 0 до 10.
    Данный аргумент является публичным и может быть изменен пользователями
    :param price: стоимость книги. Данный аргумент является защищенным
    """
    all_prod = []

    def __init__(self, number:int, name: str, rating: Union[int, float], price: Union[int, float]):
        """
        Функция инициализирует класс Products

        :param number: число, используется для выбора того или иного товара
        :param name: название книги
        :param rating: рейтинг книги
        :param price: стоимость книги
        """
        self.number = number
        self.__name = self.__check_name(name)
        self.rating = self.check_rating(rating)
        self._price = self._check_price(price)


    @staticmethod
    def __check_name(name):
        """
        Функция проверяет правильность ввода заголовка книги
        :param name: название книги
        :return: название книги
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть в формате строки")
        return name

    @staticmethod
    def check_rating(rating):
        """
        Функция проверяет правильность ввода значения рейтинга
        :param rating: значение рейтинга
        :return: значение рейтинга
        """
        if not isinstance(rating, (int, float)):
            raise TypeError("Рейтинг должен иметь численное значение")
        if rating <= 0 or rating > 10:
            raise ValueError("Рейтинг рассчитывается от 0 до 10")
        return rating

    @staticmethod
    def _check_price(price):
        """
        Функция проверяет правильность ввода цены

        :param price: значение цены
        :return: значение цены
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должен иметь численное значение")
        if price < 0:
            raise ValueError("Цена рассчитывается от 0 до 10")
        return price

    def __repr__(self) -> str:
        return f"Products({self.__name}, {self.rating}, {self._price})"

    def __str__(self) -> str:
        return f"{self.number} Название книги: {self.__check_name(self.__name)}, рейтинг: {self.check_rating(self.rating)}, " \
               f"цена: {self._check_price(self._price)}, "

    def choose_book(self):
        """Функция выбора книги. Имеет две переменные в формате словари: для выбора категории и для выбора книги.
        Позволяет сделать выбор книги несколько раз. Затем выбранные книги добавляются в массив all_prod

        :return: книгу, чей ключ соответствует введенному с клавиатуры числу
        """
        cat_dic = {1: "Children's Literature", 2: "Classics"}
        prod_dict = {1: book1, 2: book2, 3: book3, 4: book4, 5: book5}
        if cat_dic[1]:
            print(f"{prod_dict[1]},\n{prod_dict[2]}")
        if cat_dic[2]:
            print(f"{prod_dict[3]}\n{prod_dict[4]}\n{prod_dict[5]}")
        number = int(input())
        print(f"Вы выбрали пункт: {prod_dict[number]} книга добавлена в корзину.")
        Products.all_prod.append(prod_dict[number])
        print("Продолжить выбор?", 1, 2, sep="\n")
        n1 = int(input())
        if n1 == 1:
            if cat_dic[1]:
                print(f"{prod_dict[1]},\n{prod_dict[2]}")
            if cat_dic[2]:
                print(f"{prod_dict[3]}\n{prod_dict[4]}\n{prod_dict[5]}")
            number = int(input())
            print(f"Вы выбрали пункт: {prod_dict[number]} книга добавлена в корзину.")
            Products.all_prod.append(prod_dict[number])
        if n1 == 2:
            pass

        return prod_dict[number]

class Category:

    all_cat = []
    """Класс с категориями книг, представленными в магазине. """

    def __init__(self, number: int, category_name: str):
        """
        Функция инициализирует класс Category
        :param number: число, вводимое с клавиатуры, обеспечивает выбор категории
        :param category_name: имя категории
        """
        self.number = number
        self.category_name = category_name
        Category.all_cat.append(self)

    @property
    def cat_name(self):
        return self.category_name

    @cat_name.setter
    def cat_name(self, category_name: str):
        if not isinstance(category_name, str):
            raise TypeError('Категория задается строковым значением')

    def __repr__(self):
        return f"Книга добавлена к категории {self.all_cat}"

    def __str__(self):
        return f"{self.number} Категория {self.category_name}."

    def choose_cat(self, number):
        """
        Функция обеспечивает выбор категории
        :param number: число, вводимое с клавиатуры, обеспечивает выбор категории пользователем
        """
        number = int(input())
        cat_dic = {1: "Children's Literature", 2: "Classics"}
        if number == 1:
            print(f"Вы выбрали категорию {cat_dic[1]}")
        else:
            print(f"Вы выбрали категорию {cat_dic[2]}")


class Basket(Products):
    """В данном классе содержится массив купленных товаров """
    all_items = []




class User:
    """Класс User описывает пользователя книжного Интернет-магазина

    :param login: логин пользователя, используется для его аутенфикации
    :param password: пароль пользователя, используется для его аутенфикации
    """

    def __init__(self, login: Union[str, int], password: Union[str, int]):
        self.__login = self.__check_login(login)
        self.__password = self.__check_password(password)

    @staticmethod
    def __check_login(login):
        """Функция проверки правильности ввода логина"""
        if not isinstance(login, (str, int)):
            raise TypeError("Логин должен быть представлен в виде строки или числа")
        return login

    @staticmethod
    def __check_password(password):
        """Функция проверки правильности ввода пароля"""
        password1 = input('Введите пароль еще раз для проверки: ')
        if password == password1:
            print("Пароли совпадают. Вы можете выбирать книги")
        else:
            raise ValueError("Пароли не совпадают. Введите пароль заново")
            return password

    def __str__(self):
        return f"Выберите необходимую категорию"

class Purchase(Products):
    """Класс, предназначенный для совершения покупок

    :param card: номер карты покупателя
    """
    purchase = Products.all_prod

    def __init__(self, card: int):
        self.__card = self.__check_card(card)

    @staticmethod
    def __check_card(card):
        """Функция проверки правильности ввода карты"""
        if not isinstance(card, int):
            raise TypeError(f"Номер карты должен быть числом")
        if len(card) != 16:
            raise ValueError(f"В номере карты должно быть 16 цифр")

    def value_purchase(self):
        """
        Расчет стоимости покупок
        :return: стоимость покупок
        """
        cost = sum(Purchase.purchase.price)
        self.card = int(input())
        print(f"Стоимость покупок: {cost} руб. Введите номер карты {self.card}")
        print("Покупка завершена")
        return cost


if __name__ == '__main__':

    user1 = User(input("Введите Ваш логин: "), input('Введите пароль: '))
    print(user1)

    cat1 = Category(1, "Children's Literature")
    cat2 = Category(2, "Classics")
    book1 = Products(1, "Mowgli", 9.6, 344)
    book2 = Products(2, "Lord of the Rings", 8.9, 515)
    book3 = Products(3, "One Flew Over the Cuckoo's Nest", 8.8, 315)
    book4 = Products(4, "Weathering Heights", 7.6, 496)
    book5 = Products(5, "The Gadfly", 7.5, 329)

    print(cat1, cat2, sep='\n')
    print(f"Выберите категорию: ")
    Category.choose_cat(Category, 1)
    print("Выберите название книги: ")
    Products.choose_book(Products)
    print(Products.all_prod)
    print(Purchase.purchase)
    Purchase.value_purchase(Purchase)



    # print(Category.all_cat)




    #
    # card = Purchase(input("Введите номер карты: "))
