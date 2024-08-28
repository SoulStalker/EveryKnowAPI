import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.database.database import DATABASE_URL
from app.models import department, role


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    first_name: Mapped[str] = mapped_column(String(length=30), index=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=30), index=True, nullable=False)
    tg_id: Mapped[str] = mapped_column(String(length=50), index=True, nullable=False)
    # registered_at: Mapped[datetime] = mapped_column(DateTime, index=True, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey(department.c.id), nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(role.c.id), nullable=False)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
