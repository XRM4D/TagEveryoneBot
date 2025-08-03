import logging

from aiogram import Dispatcher

import core.handlers
from core.bot import BOT

def register_routers(dispatcher: Dispatcher) -> None:
    for router in core.handlers.routers:
        dispatcher.include_router(router)

def main() -> None:

    dp = Dispatcher(bot=BOT)

    register_routers(dp)

    dp.start_polling(skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    main()