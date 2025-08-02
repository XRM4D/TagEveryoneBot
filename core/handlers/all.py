from aiogram import Router
from aiogram.types import BotCommand, Message

all_router = Router()

@all_router.message(BotCommand(command="all", description="Тэг всех пользователей"))
async def all_handler(message: Message):
    chat = await message.chat

