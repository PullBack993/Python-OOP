class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def __str__(self):
        return f"{self.title} by {self.author}"


class BookReader:
    def __init__(self, book):
        self.book = book
        self.page = 0

    def change_page(self, page):
        self.page = page


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if title == book.title:
                return book

the_godfather = Book('The Godfather', 'Mario Puzo')
principles = Book('Principles', 'Ray Dalio')

library = Library([the_godfather, principles])
print(library.find_book('Principles'))