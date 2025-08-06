import logging

from aiogram import Router
from aiogram.types import ChatMemberUpdated

from core.bot import BOT
from database.chats import Chat
from database.users import User

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

    member = await User.get_by_telegram_id(chat_member.from_user.id)

    await add_chat_to_user(
        member,
        chat_member.from_user.id,
        chat_member.from_user.username,
        chat_member.chat.id
    )

    await BOT.send_message(chat_id=chat.id, text="PLACEHOLDER")


@on_member_update_router.chat_member()
async def process_new_member(chat_member: ChatMemberUpdated):


    chat = await Chat.get(chat_member.chat.id)
    if not chat:
        return

    await chat.add_member(chat_member.new_chat_member.id)

    member = await User.get_by_telegram_id(chat_member.new_chat_member.user.id)

    await add_chat_to_user(
        member,
        chat_member.new_chat_member.user.id,
        chat_member.new_chat_member.user.username,
        chat_member.chat.id
    )


async def add_chat_to_user(member: User, telegram_id: int, username: str, chat_id: int) -> None:

    logger.info(f"Adding chat {telegram_id} to user {username}")

    if not member:
        new_user = User(
            telegram_id=telegram_id,
            username=username,
            assigned_chats={"chats": [chat_id]}
        )

        await User.add(new_user)

    else:
        logger.info(f"User with id {telegram_id} already exists")
        member.add_chat(chat_id)