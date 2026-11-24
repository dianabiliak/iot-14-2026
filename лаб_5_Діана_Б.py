"""Модуль для моделювання книг та роботи книжкового магазину."""

class Book:
    """Клас, що представляє книгу та її характеристики."""

    def __init__(self, title, price, number_of_pages, author, quantity, number_of_sales):
        self.title = title
        self.price = price 
        self.number_of_pages = number_of_pages
        self.author = author
        self.quantity = quantity
        self.number_of_sales = number_of_sales
        """Ініціалізує об'єкт книги."""
        
    def __del__(self):
        print(f"Книга {self.title} була видалена з пам'яті")
        """Повідомляє про видалення об'єкта книги з пам'яті."""

    def __str__(self):
     """Повертає текстове представлення інформації про книгу."""
     return (
        f"Назва: {self.title}, ціна: {self.price}, "
        f"кількість сторінок: {self.numberOfPages}, "
        f"автор: {self.author}, кількість: {self.quantity}, "
        f"кількість продажів: {self.numberOfSales}"
    )

class BookShop:
    """Клас для управління асортиментом книжкового магазину."""

    def __init__(self):
        """Ініціалізує порожній список книг у магазині."""
        self.books = []

    def add_book(self, book):
        """Додає книгу до асортименту магазину."""
        self.books.append(book)
        print(f"Книгу {book} додано до магазину")

    def remove_book(self, book):
        """Вилучає вказану книгу з асортименту магазину."""
        self.books.remove(book)
        print(f"Книгу {book} вилучено з магазину")

    def top_price(self, n=3):
        """Виводить топ-n найдорожчих книг у магазині."""
        sorted_price_lst = sorted(self.books, key=lambda b: b.price, reverse= True)
        print(f"ТОП-{n} КНИГИ ЗА ЦІНОЮ:")
        for book in sorted_price_lst[:n]:
            print(book)

    def top_sales(self, n=3):
        """Виводить топ-n книг за кількістю продажів."""
        sorted_sales_lst = sorted(self.books, key=lambda b: b.number_of_sales, reverse= True)
        print(f"ТОП-{n} КНИГИ ЗА КІЛЬКІСТЮ ПРОДАЖІВ:")
        for book in sorted_sales_lst[:n]:
            print(book)


def main():
    """Демонструє створення книг, роботу магазину та формування рейтингів."""
    book1 = Book('Кобзар', 450, 550, 'Тарас Шевченко', 16, 30)
    book2 = Book('1984', 220, 368, 'Джордж Орвелл', 12, 50)
    book3 = Book('Тлумач тіл', 620, 528, 'Антоніо Гаррідо', 1, 3)
    book4 = Book('Лісова пісня', 340, 424, 'Леся Українка', 9, 18)
    book5 = Book('Шість багряних журавлів', 750, 448, 'Елізабет Лім', 2, 2)
    shop = BookShop()
    shop.add_book(book1)
    shop.add_book(book2)
    shop.add_book(book3)
    shop.add_book(book4)
    shop.add_book(book5)
    shop.top_price()
    shop.top_sales()
    shop.remove_book(book3)
    del book3


if __name__ == '__main__':
    main()
