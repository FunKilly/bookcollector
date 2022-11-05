import datetime
from typing import Optional


class Category:
    def __init__(self, name: str):
        self.name = name


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        publisher: str,
        category_id: Optional[int],
        release_date: Optional[datetime.date],
        isbn: str,
    ):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.category_id = category_id
        self.release_date = release_date
        self.isbn = isbn
        self.reviews = []


class Rating:
    def __init(self, rate: int, book_id: str):
        self.rate = rate
        self.book_id = book_id
