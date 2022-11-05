from portal.domain.commands import AddBook, AddRate, GetBook, ListBooks
from portal.domain.models import Book, Rating
from portal.services.uow import SqlAlchemyUnitOfWork


def add_book(cmd: AddBook, uow: SqlAlchemyUnitOfWork):
    with uow:
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
            return uow.books.get_by_isbn(cmd.book_id)
        return uow.books.get(cmd.book_id)


def list_books(cmd: ListBooks, uow: SqlAlchemyUnitOfWork):
    with uow:
        return uow.books.get_all()


def add_rate(cmd: AddRate, uow: SqlAlchemyUnitOfWork):
    with uow:
        if book := uow.books.get(cmd.book_id):
            book.reviews.append(Rating(book_id=book.id, rate=cmd.rate))
        uow.commit()


COMMAND_HANDLERS = {
    AddBook: add_book,
    AddRate: add_rate,
    GetBook: get_book,
    ListBooks: list_books,
}
