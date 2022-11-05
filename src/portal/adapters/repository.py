import abc
from typing import List

from portal.domain.models import Book, Category


class AbstractRepository(abc.ABC):
    def add(self, book: Book):
        self._add(book)

    def get(self, book_id: int) -> Book:
        return self._get(book_id)

    def get_by_category(self, category_id: int) -> Book:
        return self._get_by_category(category_id)

    def get_by_isbn(self, isbn: str) -> Book:
        return self._get_by_category(isbn)

    def get_all(self) -> List[Book]:
        return self._get_all()

    @abc.abstractmethod
    def _add(self, book: Book):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, book_id: int) -> Book:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_by_category(self, category_id: int) -> List[Book]:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_by_isbn(self, isbn: str) -> Book:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_all(self, isbn: str) -> List[Book]:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, book):
        self.session.add(book)

    def _get(self, book_id):
        return self.session.query(Book).filter_by(id=book_id).first()

    def _get_by_category(self, category_id):
        return self.session.query(Book).filter_by(Category.id == category_id).all()

    def _get_by_isbn(self, isbn):
        return self.session.query(Book).filter_by(isbn == isbn).all()

    def _get_all(self):
        return self.session.query(Book).all()
