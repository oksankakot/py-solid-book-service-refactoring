from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_content(self, title: str, content: str) -> None:
        pass


class ConsolePrinter(Printer):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrinter(Printer):
    def print_content(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])
