import asyncio
import os

from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    load_dotenv()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')