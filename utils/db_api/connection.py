import asyncio
from typing import Sequence
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db_api.base import Base
from utils.db_api.models import User, Channel, Audio, Admin

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
                    username=username,
                    first_name=first_name
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

    # ---Channel model---

    async def reg_channel(self, chat_id, title):
        """Регистрация channel"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                Channel(
                    chat_id=chat_id,
                    title=title
                )
            )
            await session.commit()


    async def get_channel(self, chat_id) -> Channel:
        """Получения пользователя"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.get(Channel, chat_id)
            return response

    # ---Audio model---

    async def reg_audio(self, chat_id, text, dist):
        """Регистрация audio"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                Audio(
                    chat_id=chat_id,
                    text=text,
                    distination=dist
                )
            )
            await session.commit()


    async def get_audio(self, chat_id) -> Audio:
        async with self.async_session() as session:
            session: AsyncSession
            response = await session.execute(select(Audio).where(Audio.chat_id==chat_id))
            return response.scalars().all()

    # ADMINS

    async def get_admin(self, username, password):
        async with self.async_session() as session:
            session: AsyncSession
            response = await session.execute(select(Admin).where(Admin.username==username, Admin.password==password))
            return response.scalar()