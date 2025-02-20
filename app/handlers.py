from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from .main import get_link

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('hello there')


@router.message(Command('schedule'))
async def get_schedule(message: Message):
    try:
        link = get_link(course=0, week=1)
        await message.answer_document(link)
    except:
        await message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")


@router.message(Command('help'))
async def help(message: Message):
    await message.answer("Для получения рассписаня нажниме на одну из кнопок в меню, или введите команду /schedule \
                         \n\nНа данный момент бот может отправлять только рассписание первых курсов на след. неделю.\
                         Позже появится возможность выбрать курс и расписание какой недели необходимо отправить(текущей или следующей)")
