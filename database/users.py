from __future__ import annotations

from sqlalchemy import Column, Integer, BIGINT, VARCHAR, JSON

from database import Base, Session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BIGINT, nullable=False, primary_key=True)
    username = Column(VARCHAR(255), nullable=True)
    assigned_chats = Column(JSON, nullable=False, default='"chats": []')


    @staticmethod
    async def add(user: User) -> None:
        with Session() as session:
            session.add(user)
            session.commit()

    @staticmethod
    async def get_by_telegram_id(telegram_id: int) -> User | None:
        with Session() as session:
            return session.query(User).filter(User.telegram_id == telegram_id).one_or_none()

    @staticmethod
    async def delete_by_telegram_id(telegram_id: int) -> None:
        with Session() as session:
            session.query(User).filter(User.telegram_id == telegram_id).delete()

