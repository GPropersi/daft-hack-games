from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from main import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]