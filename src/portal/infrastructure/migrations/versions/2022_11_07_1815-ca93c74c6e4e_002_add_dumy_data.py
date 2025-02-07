"""002_add_dumy_data

Revision ID: ca93c74c6e4e
Revises: 20b91223c052
Create Date: 2022-11-07 18:15:16.539267

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "ca93c74c6e4e"
down_revision = "20b91223c052"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.execute(
        "INSERT INTO categories (name) VALUES ('Thriller'), ('Sci-Fi'), ('Fantasy'), ('Non-Fiction')"
    )
    op.execute(
        """INSERT INTO books (title, author, publisher, release_date, isbn) VALUES
        ('Hyperion', 'Dan Simmons', 'Mag' ,'2015-09-09','ISBN-9788374805575'),
        ('A Treatise on Shelling Beans', 'Wieslaw Mysliwski', 'ZNAK' ,'2021-06-25','ISBN-9788324055326'),
        ('Neuromancer', 'William Gibson', 'Mag' ,'1992-01-01','ISBN-9788324577750'),
        ('Horus Rising', 'Dan Abnett', 'Copernicus Corp','2007-01-01','ISBN-9788375746198')"""
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
