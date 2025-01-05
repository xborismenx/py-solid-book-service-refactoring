from abc import abstractmethod, ABC



class BookContentDisplay(ABC):
    @abstractmethod
    def read(self):
        pass


class BookContentConsole(BookContentDisplay):
    def __init__(self, book) -> None:
        self.content = book.content

    def read(self):
        print(self.content)


class BookContentReverse(BookContentDisplay):
    def __init__(self, book) -> None:
        self.content = book.content

    def read(self):
        print(self.content[::-1])

class BookContent:
    @staticmethod
    def method_print(book, method_type: str) -> None:
        if method_type == "console":
            BookContentConsole(book).read()
        elif method_type == "reverse":
            BookContentReverse(book).read()



class BookPrint(ABC):
    @abstractmethod
    def print_book(self):
        pass


class BookPrintConsole(BookPrint):
    def __init__(self, book) -> None:
        self.title = book.title
        self.content = book.content

    def print_book(self):
        print(f"Printing the book: {self.title}...")
        print(self.content)


class BookPrintReverse(BookPrint):
    def __init__(self, book) -> None:
        self.title = book.title
        self.content = book.content

    def print_book(self):
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])


class BookPrint:
    @staticmethod
    def method_print(book, method_type: str) -> None:
        if method_type == "console":
            BookPrintConsole(book).print_book()
        elif method_type == "reverse":
            BookPrintReverse(book).print_book()

