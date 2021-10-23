class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class AuthorFormatter:
    def format(self, book: Book) -> str:
        return book.author


class Printer:
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book

    def get_author(self, book):
        formatter = AuthorFormatter()
        return formatter.format(book)


book = Book('Principles', 'Ray Dalio', 'Lorem ipsun')
printer = Printer()
print(printer.get_author(book))
