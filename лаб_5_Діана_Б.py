class Book:

    def __init__(self, title, price, numberOfPages, author, quantity, numberOfSales):
        self.title = title
        self.price = price 
        self.numberOfPages = numberOfPages
        self.author = author
        self.quantity = quantity
        self.numberOfSales = numberOfSales
        
    def __del__(self):
        print(f"Книга {self.title} була видалена з пам'яті")

    def __str__(self):
        return f"Назва: {self.title}, ціна: {self.price}, кількість сторінок: {self.numberOfPages}, автор: {self.author}, кількість: {self.quantity}, кількість продажів: {self.numberOfSales}"


class BookShop:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу {book} додано до магазину")

    def remove_book(self, book):
        self.books.remove(book)
        print(f"Книгу {book} вилучено з магазину")

    def top_price(self, n = 3):
        sorted_price_lst = sorted(self.books, key= lambda b: b.price, reverse= True)
        print("ТОП-3 КНИГИ ЗА ЦІНОЮ:")
        for book in sorted_price_lst[:n]:
            print(book)

    def top_sales(self, n = 3):
        sorted_sales_lst = sorted(self.books, key= lambda b: b.numberOfSales, reverse= True)
        print("ТОП-3 КНИГИ ЗА КІЛЬКІСТЮ ПРОДАЖІВ:")
        for book in sorted_sales_lst[:n]:
            print(book)


def main():
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