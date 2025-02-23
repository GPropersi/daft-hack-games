from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase
from app import db

class Users(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)

    stats = relationship("UserStats", back_populates="user")

class UserStats(db.Model):
    __tablename__ = "user_stats"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    minutes: Mapped[int] = mapped_column(Integer)
    category: Mapped[int] = mapped_column(ForeignKey("category.id"))

    user = relationship("Users", back_populates="stats")
    

class Category(db.Model):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    
