import uuid

from fastapi import APIRouter

from src.app_1.domain.models.books import Author, Book

router = APIRouter()


@router.get("/books")
async def read_books():
    author = Author(pk=uuid.uuid4(), name="Oskar", surname="Kowalczyk")
    book_1, book_2 = (
        Book(pk=uuid.uuid4(), title="Poezja Romantyczna", author=author),
        Book(pk=uuid.uuid4(), title="Fizyka Kwantowa", author=author),
    )
    return [book_1, book_2]
