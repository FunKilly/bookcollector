import logging

from sqlalchemy import (Column, Date, ForeignKey, Integer, MetaData, String,
                        Table)
from sqlalchemy.orm import mapper, relationship

from portal.domain import models

logger = logging.getLogger(__name__)

metadata = MetaData()

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255), nullable=False),
    Column("author", String(150), nullable=False),
    Column("category", ForeignKey("categories.id")),
    Column("release_date", Date),
    Column("isbn", String(40)),
)


categories = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50), nullable=False),
)

ratings = Table(
    "ratings",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("rate", String(50), nullable=False),
    Column("book_id", ForeignKey("books.id")),
)


def start_mappers():
    ratings_mapper = mapper(
        models.Rating,
        ratings,
    )
    books_mapper = mapper(
        models.Book, books, properties={"ratings": relationship(ratings_mapper)}
    )
    mapper(models.Category, categories, properties={"books": relationship(books_mapper)})
