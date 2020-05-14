import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


def connect():
    engine = sa.create_engine(DB_PATH)
    session = sessionmaker(engine)()
    return session


def find_art(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums


def find_alb(album):
    """
    Поиск альбома в базе данных
    """
    session = connect()
    if session.query(Album).filter(Album.album == album).first():
        return "Такой альбом уже существует"
    return "OK"


def insert(alb):
    session = connect()
    session.add(alb)
    session.commit()
    return "Данные записаны"