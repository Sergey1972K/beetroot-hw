# Task_2
# Library

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, title, year, author):
        """Створює нову книгу і додає її до бібліотеки."""
        book = Book(title, year, author)
        self.add_book(book)
        return book

    def add_book(self, book):
        """Додає книгу до бібліотеки."""
        self.books.append(book)
        if book.author not in self.authors:
            self.authors.append(book.author)

    def group_by_author(self, author):
        """Вибирає всі книги певного автора."""
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        """Вибирає всі книги певного року видання."""
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return (
            f"Library: {self.name}, Books: {len(self.books)},\n"
            f"Authors: {len(self.authors)}"
        )

    def __repr__(self):
        return (
            f"Library(name={self.name}, books={len(self.books)},\n"
            f"authors={len(self.authors)})"
        )


class Book:
    total_books = 0  # Змінна класу для підрахунку загальної кількості книг

    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author
        Book.total_books += 1  # Збільшується при створенні нової книги

    def __str__(self):
        return f"'{self.title}' by {self.author.name}, {self.year}"

    def __repr__(self):
        return (
            f"Book(title={self.title}, year={self.year},\n"
            f"author={repr(self.author)})"
        )


class Author:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = birthdate
        self.books = []

    def add_book(self, book):
        """Додає книгу до списку книг автора."""
        self.books.append(book)

    def __str__(self):
        return f"{self.name} ({self.country}), born on {self.birthdate}"

    def __repr__(self):
        return (
            f"Author(name={self.name}, country={self.country},\n"
            f"birthdate={self.birthdate})"
        )


# Приклад використання
library = Library("City Library")

author1 = Author("Василь Шкляр", "Україна", "1951-01-03")
author2 = Author("Ліна Костенко", "Україна", "1930-03-19")
author3 = Author("Іван Франко", "Україна", "1856-08-27")

book1 = library.new_book("Чорний ворон", 2009, author1)
book2 = library.new_book("Записки українського самашедшого", 2010, author2)
book3 = library.new_book("Захар Беркут", 1883, author3)
book4 = library.new_book("Книга готується штурм", 2008, author1)

# Додаємо книги до авторів
author1.add_book(book1)
author1.add_book(book4)
author2.add_book(book2)
author3.add_book(book3)

print(library)  # Виведе інформацію про бібліотеку
print(f"Total books: {Book.total_books}")  # Виведе: Total books: 4

print("\nBooks by Василь Шкляр:")
for book in library.group_by_author(author1):
    print(book)  # Виведе книги Василя Шкляра

print("\nBooks by Ліна Костенко:")
for book in library.group_by_author(author2):
    print(book)  # Виведе книги Ліни Костенко

print("\nBooks by Іван Франко:")
for book in library.group_by_author(author3):
    print(book)  # Виведе книги Івана Франка

print("\nBooks from 2009:")
for book in library.group_by_year(2009):
    print(book)  # Виведе книги 2009 року
