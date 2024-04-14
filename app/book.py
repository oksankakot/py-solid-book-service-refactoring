from app.display_book import DisplayStrategy
from app.print_book import Printer
from app.serializer_book import Serializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self, strategy: DisplayStrategy) -> None:
        print(strategy.display(self.content))

    def print_book(self, printer: Printer) -> None:
        printer.print_content(self.title, self.content)

    def serialize(self, serializer: Serializer) -> str:
        return serializer.serialize(self.title, self.content)
