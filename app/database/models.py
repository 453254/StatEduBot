from sqlalchemy import func, BigInteger, DateTime, Boolean, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from datetime import date

import os
from dotenv import load_dotenv

load_dotenv()
engine = create_async_engine(url=os.getenv('SQLALCHEMY_DATABASE_URL'))


async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class Guest(Base):
    __tablename__ = 'guests'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    date = mapped_column(DateTime, default=func.now())


class Users_Subject(Base):
    __tablename__ = 'subjects'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

    math = mapped_column(Boolean, default=False)
    russian = mapped_column(Boolean, default=False)
    informatics = mapped_column(Boolean, default=False)
    physics = mapped_column(Boolean, default=False)
    chemistry = mapped_column(Boolean, default=False)
    biology = mapped_column(Boolean, default=False)
    geography = mapped_column(Boolean, default=False)
    history = mapped_column(Boolean, default=False)
    social = mapped_column(Boolean, default=False)
    literature = mapped_column(Boolean, default=False)
    english = mapped_column(Boolean, default=False)
    german = mapped_column(Boolean, default=False)
    french = mapped_column(Boolean, default=False)
    spanish = mapped_column(Boolean, default=False)


class User_Resoult(Base):
    __tablename__ = 'resoults'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    subject = mapped_column(String)
    resoult: Mapped[int] = mapped_column()
    date = mapped_column(Date, default=func.now())


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)