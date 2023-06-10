import asyncio
from typing import Sequence
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db_api.base import Base
from utils.db_api.models import User, Talent, Recruiter

from data.config import DATABASE_URL


class Database:
    def get_engine(self):
        engine = create_async_engine(
            DATABASE_URL,
            future=True
        )

        return engine

    async def load(self) -> AsyncSession:
        engine= self.get_engine()

        async_sessionmaker = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )

        self.async_session = async_sessionmaker

    # ---User model---

    async def reg_user(self, user_id: str, username: str, first_name: str):
        """Регистрация пользователя"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                User(
                    user_id=user_id,
                    username=username
                )
            )
            await session.commit()

    async def get_user(self, user_id) -> User:
        """Получения пользователя"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.get(User, user_id)
            return response
    
    async def get_all_users(self) -> Sequence[User]:
        """Получения всех пользователей"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.execute(select(User))
            return response.scalars().all()

    # ---Talent model---

    async def reg_talent(self, user_id, fullname):
        """Регистрация channel"""
        async with self.async_session() as session:
            session: AsyncSession

            talent = Talent(fullname=fullname)
            user = await session.execute(select(User).where(User.user_id == user_id))
            talent.user = user.scalar_one()
            await session.merge(talent)

            await session.commit()

    # ---Audio model---

    async def reg_recruiter(self, user_id, fullname, company):
        """Регистрация audio"""
        async with self.async_session() as session:
            session: AsyncSession
            recruiter = Recruiter(fullname=fullname, company=company)
            user = await session.execute(select(User).where(User.user_id == user_id))
            recruiter.user = user.scalar_one()
            await session.merge(recruiter)

            await session.commit()