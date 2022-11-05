from fastapi import FastAPI

from portal.bootstrap import bootstrap
from portal.domain import commands

app = FastAPI()
bus = bootstrap()


@app.get("/")
def index():
    return "Happy Path"


@app.post("/books")
def add_book(book: dict):
    cmd = commands.AddBook(**book)
    bus.handle(cmd)


@app.get("/books/{book_id}")
def get_book(book_id: str):
    cmd = commands.GetBook(book_id)
    return bus.handle(cmd)


@app.get("/books")
def get_books():
    cmd = commands.ListBooks()
    return bus.handle(cmd)


@app.post("/books/{book_id}/review")
def add_rate(book_id, rate):
    cmd = commands.AddRate(book_id, rate)
    bus.handle(cmd)
