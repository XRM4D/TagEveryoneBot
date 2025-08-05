from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from settings.config import BOT_NAME


def get_start_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    admin_permissions = "post_messages"

    chat_url = f"https://t.me/{BOT_NAME}?startgroup&admin={admin_permissions}"

    builder.row(
        InlineKeyboardButton(
            text="➕ Добавить бота в чат",
            url=chat_url
        )
    )

    return builder.as_markup()