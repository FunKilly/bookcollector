from uuid import UUID

from pydantic import BaseModel


class Author(BaseModel):
    pk: UUID
    name: str
    surname: str


class Book(BaseModel):
    pk: UUID
    title: str
    author: Author
