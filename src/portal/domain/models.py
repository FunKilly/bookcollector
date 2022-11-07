import datetime
from statistics import mean
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
        self.ratings = []
        self.category = None

    def convert_into_dict(self) -> dict:
        model_as_dict = {
            key: value for key, value in vars(self).items() if not key.startswith("_")
        }
        if self.ratings:
            model_as_dict["average_rate"] = self._get_average_rate()

        if self.category:
            model_as_dict["category"] = {
                "id": self.category.id,
                "name": self.category.name,
            }

        return model_as_dict

    def _get_average_rate(self) -> float:
        return mean([rating.rate for rating in self.ratings])


class Rating:
    def __init__(self, rate: int, book_id: str):
        self.rate = rate
        self.book_id = book_id
