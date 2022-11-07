from fastapi import APIRouter

from portal.bootstrap import bootstrap
from portal.domain import commands
from portal.infrastructure import serializers

bus = bootstrap()
router = APIRouter()


@router.get("/")
def index():
    return "Happy Path"


@router.post("/books", status_code=201)
def add_book(request: serializers.CreateBookRequest):
    cmd = commands.AddBook(**request.dict())
    bus.handle(cmd)
    return {"message": "ok"}


@router.get("/books/{book_id}")
def get_book(book_id: str):
    cmd = commands.GetBook(book_id)
    book = bus.handle(cmd)
    return serializers.Book(**book)


@router.get("/books")
def get_books():
    cmd = commands.ListBooks()
    books = bus.handle(cmd)
    return [serializers.Book(**book) for book in books]


@router.post("/books/{book_id}/review", status_code=201)
def add_rate(book_id, request: serializers.CreateRateRequest):
    cmd = commands.AddRate(book_id=book_id, rate=request.rate)
    bus.handle(cmd)
    return {"message": "ok"}
