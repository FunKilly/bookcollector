import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class CreateBookRequest(BaseModel):
    title: str
    author: str
    publisher: str
    isbn: str
    category_id: Optional[int] = None
    release_date: Optional[datetime.date] = None

    @validator("isbn")
    def isbn_must_starts_with_isbn_prefix(cls, v):
        if not v.startswith("ISBN"):
            raise ValueError("ISBN have incorrect format")
        return v.title()


class CreateRateRequest(BaseModel):
    rate: int = Field(ge=1, le=10)


class Category(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    isbn: str
    category: Optional[Category] = None
    release_date: Optional[datetime.date] = None
    average_rate: float = 0.0
