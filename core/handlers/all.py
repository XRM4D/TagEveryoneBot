from aiogram import Router
from aiogram.filters import Command
from aiogram.types import BotCommand, Message

all_router = Router()

@all_router.message(Command("all"))
async def all_handler(message: Message):
    chat = await message.chat
    if chat.type in ["group", "supergroup"]:
        pass#TODO

