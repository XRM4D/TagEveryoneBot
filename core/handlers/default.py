from aiogram import types
from aiogram import Router
from aiogram.filters import CommandStart

from core.keyboards.default import get_start_keyboard
from database.users import User

default_router = Router()

@default_router.message(CommandStart())
async def start_handler(message: types.Message):

    user = await User.get_by_telegram_id(message.from_user.id)
    if not user:
        new_user = User(
            telegram_id=message.from_user.id,
            username=message.from_user.username
        )

        await User.add(new_user)

    hello_text = "PLACEHOLDER"

    await message.answer(hello_text, reply_markup=get_start_keyboard())
