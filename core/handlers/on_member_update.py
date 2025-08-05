import logging

from aiogram import Router
from aiogram.enums import ChatMemberStatus
from aiogram.types import ChatMemberUpdated, User

from core.bot import BOT
from database.chats import Chat

logger = logging.getLogger(__name__)

on_member_update_router = Router()

@on_member_update_router.my_chat_member()
async def process_new_chat(chat_member: ChatMemberUpdated):

    me = await BOT.get_me()

    if chat_member.new_chat_member.user.id != me.id:
        return

    chat = chat_member.chat

    if chat_member.new_chat_member.status != "administrator":
        await Chat.delete(chat.id)
        return

    new_chat = Chat(
        telegram_id=chat.id,
        members={"members": [chat_member.from_user.id]}
    )
    await Chat.add(new_chat)
    await BOT.send_message(chat_id=chat.id, text="PLACEHOLDER")


@on_member_update_router.chat_member()
async def process_new_member(chat_member: ChatMemberUpdated):


    chat = await Chat.get(chat_member.chat.id)
    if not chat:
        return

    await chat.add_member(chat_member.new_chat_member.id)
