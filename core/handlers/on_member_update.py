import json

from aiogram import Router
from aiogram.types import ChatMemberUpdated, User

from core.bot import BOT
from database.chats import Chat

on_member_update_router = Router()

@on_member_update_router.my_chat_member()
async def on_member_update(chat_member: ChatMemberUpdated):

    me = await BOT.get_me()

    if chat_member.new_chat_member.user.id == me.id:
        await process_new_chat(chat_member)
    else:
        await process_new_member(chat_member)



async def process_new_chat(chat_member: ChatMemberUpdated):
    chat = chat_member.chat

    new_chat = Chat(
        telegram_id=chat.id,
        members=f'"members": [{chat_member.from_user.id}]'
    )
    await Chat.add(new_chat)
    await BOT.send_message(chat_id=chat.id, text="PLACEHOLDER")

async def process_new_member(chat_member: ChatMemberUpdated):
    pass

