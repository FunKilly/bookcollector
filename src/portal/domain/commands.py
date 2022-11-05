import datetime
from dataclasses import dataclass
from typing import Optional


class Command:
    pass


@dataclass
class AddRate(Command):
    book_id: id
    rate: id


@dataclass
class AddBook(Command):
    title: str
    author: str
    publisher: str
    category_id: Optional[id]
    release_date: Optional[datetime.date]
    isbn: str


@dataclass
class GetBook(Command):
    book_id: int


@dataclass
class ListBooks(Command):
    pass
