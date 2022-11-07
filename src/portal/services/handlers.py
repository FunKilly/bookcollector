from portal.domain.commands import AddBook, AddRate, GetBook, ListBooks
from portal.domain.models import Book, Rating
from portal.services.uow import SqlAlchemyUnitOfWork
from portal.utils.exceptions import BookAlreadyExists, BookNotFound


def add_book(cmd: AddBook, uow: SqlAlchemyUnitOfWork):
    with uow:
        if uow.books.get_by_isbn(cmd.isbn):
            raise BookAlreadyExists
        uow.books.add(
            Book(
                title=cmd.title,
                author=cmd.author,
                publisher=cmd.publisher,
                category_id=cmd.category_id,
                release_date=cmd.release_date,
                isbn=cmd.isbn,
            )
        )
        uow.commit()


def get_book(cmd: GetBook, uow: SqlAlchemyUnitOfWork):
    with uow:
        if cmd.book_id.startswith("ISBN"):
            book = uow.books.get_by_isbn(cmd.book_id)
        else:
            book = uow.books.get(cmd.book_id)

        if not book:
            raise BookNotFound

        return book.convert_into_dict()


def list_books(cmd: ListBooks, uow: SqlAlchemyUnitOfWork):
    with uow:
        books = uow.books.get_all()
        return [book.convert_into_dict() for book in books]


def add_rate(cmd: AddRate, uow: SqlAlchemyUnitOfWork):
    with uow:
        if book := uow.books.get(cmd.book_id):
            book.ratings.append(Rating(rate=cmd.rate, book_id=book.id))
        uow.commit()


COMMAND_HANDLERS = {
    AddBook: add_book,
    AddRate: add_rate,
    GetBook: get_book,
    ListBooks: list_books,
}
