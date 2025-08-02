from aiogram import Bot
from settings.config import BOT_TOKEN

BOT = Bot(BOT_TOKEN)

BOT_NAME = BOT.get_my_name()