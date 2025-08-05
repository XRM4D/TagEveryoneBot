import asyncio
import logging

from aiogram import Dispatcher

import core.handlers
from core.bot import BOT
from database import init_db


def register_routers(dispatcher: Dispatcher) -> None:
    for router in core.handlers.routers:
        dispatcher.include_router(router)

async def main() -> None:

    init_db()

    dp = Dispatcher()

    register_routers(dp)

    await dp.start_polling(BOT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    asyncio.run(main())