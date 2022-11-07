import datetime
from dataclasses import dataclass
from typing import Optional


class Command:
    pass


@dataclass
class AddRate(Command):
    book_id: id
    rate: int


@dataclass
class AddBook(Command):
    title: str
    author: str
    publisher: str
    isbn: str
    category_id: Optional[id] = None
    release_date: Optional[datetime.date] = None


@dataclass
class GetBook(Command):
    book_id: int


@dataclass
class ListBooks(Command):
    pass
