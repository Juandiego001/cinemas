from core.app import db
from bcrypt import checkpw
from sqlalchemy import BigInteger, Integer, String, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(450), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    document: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())

    def check_password(self, in_pw, db_pw):
        return checkpw(in_pw, db_pw)


class Group(db.Model):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())


class UserGroup(db.Model):
    __tablename__ = 'user_groups'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int]
    group_id: Mapped[int]


class Module(db.Model):
    __tablename__ = 'modules'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())


class Permission(db.Model):
    __tablename__ = 'permissions'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    read: Mapped[bool] = mapped_column()
    create: Mapped[bool]
    update: Mapped[bool]
    delete: Mapped[bool]


class Category(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
    

class Chair(db.Model):
    __tablename__ = 'chairs'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    cell: Mapped[str] = mapped_column(String(3), nullable=False)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
    

class Movie(db.Model):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=True)
    classification_age: Mapped[int] = mapped_column(Integer, nullable=True)
    category_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('categories.id'))
    trailer_video: Mapped[str] = mapped_column(String(), nullable=True)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
    

class Room(db.Model):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
    

class Schedule(db.Model):
    __tablename__ = 'schedules'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    start_date: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
    

class Ticket(db.Model):
    __tablename__ = 'tickets'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    start_date: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    status: Mapped[str] = mapped_column(String(20), 
                                        nullable=False,
                                        default='ACTIVE')
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(), 
        nullable=False,
        default=lambda: datetime.now(),
        onupdate=lambda: datetime.now())
