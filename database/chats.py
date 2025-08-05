from __future__ import annotations

import json

from sqlalchemy import Column, Integer, JSON, BIGINT

from database import Base, Session


class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BIGINT, primary_key=True)
    members = Column(JSON, nullable=True, default='"members": []')


    async def get_members(self) -> list[int]:
        return json.load(self.members).get("members", [])

    @staticmethod
    async def add(chat: Chat):
        with Session() as session:
            session.add(chat)
            session.commit()

    @staticmethod
    async def get(chat_id: int) -> Chat | None:
        with Session() as session:
            return session.query(Chat).filter(Chat.id == chat_id).one_or_none()



