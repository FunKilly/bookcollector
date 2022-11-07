from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse

from portal.bootstrap import bootstrap
from portal.domain import commands
from portal.infrastructure import serializers

app = FastAPI()
bus = bootstrap()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    if isinstance(exc, RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
        )
    return PlainTextResponse(exc.message, status_code=400)


@app.get("/")
def index():
    return "Happy Path"


@app.post("/books", status_code=201)
def add_book(request: serializers.CreateBookRequest):
    cmd = commands.AddBook(**request.dict())
    bus.handle(cmd)
    return {"message": "ok"}


@app.get("/books/{book_id}")
def get_book(book_id: str):
    cmd = commands.GetBook(book_id)
    book = bus.handle(cmd)
    return serializers.Book(**book)


@app.get("/books")
def get_books():
    cmd = commands.ListBooks()
    books = bus.handle(cmd)
    return [serializers.Book(**book) for book in books]


@app.post("/books/{book_id}/review", status_code=201)
def add_rate(book_id, request: serializers.CreateRateRequest):
    cmd = commands.AddRate(book_id=book_id, rate=request.rate)
    bus.handle(cmd)
    return {"message": "ok"}
