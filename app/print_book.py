from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print_content(self, title: str, content: str) -> None:
        pass


class ConsolePrinter(Printer):
    def __init__(self, book: Book) -> None:
        self._book = book

    def print_book(self) -> None:
        print(f"Printing the book: {self._book.title}...")
        print(self._book.content)


class ReversePrinter(Printer):
    def __init__(self, book: Book) -> None:
        self._book = book

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self._book.title}...")
        print(self._book.content[::-1])
