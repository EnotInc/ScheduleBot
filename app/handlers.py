from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from .main import get_link
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Привет! Этот бот создан для упрощения твоей жинзи в колледже. Для его использования тебе достаточно просто выбрать один из пунктов в меню",reply_markup=kb.main)


@router.message(F.text == "Расписание на эту неделю")
async def get_this_schedule(message: Message):
    await message.answer("Расписание какого курса вам нужно?", reply_markup=kb.course_this)

@router.callback_query(F.data == 'first_this')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=0, week=0)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except:
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")

@router.callback_query(F.data == 'second_this')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=1, week=0)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except:
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")

@router.callback_query(F.data == 'third_this')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=2, week=0)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except:
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")

@router.callback_query(F.data == 'last_this')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=2, week=0)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except:
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")



@router.message(F.text == "Расписание на след. неделю")
async def get_next_schedule(message: Message):
    await message.answer("Расписание какого курса вам нужно?", reply_markup=kb.course_next)

@router.callback_query(F.data == 'first_next')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=0, week=1)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except: 
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")

@router.callback_query(F.data == 'second_next')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=1, week=1)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except:
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")

@router.callback_query(F.data == 'third_next')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=2, week=1)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except:
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")

@router.callback_query(F.data == 'last_next')
async def first_this(callback: CallbackQuery):
    await callback.answer('')
    try:
        link = get_link(course=2, week=1)
        await callback.message.edit_reply_markup(reply_markup=None)
        await callback.message.delete()
        await callback.message.answer_document(link)
    except:
        await callback.message.answer("Что-то пошло не так и нам не удалось найти рассписание. Присим прощения")


@router.message(Command('help'))
async def help(message: Message):
    await message.answer("Для получения рассписаня нажниме на одну из кнопок в меню, или введите команду /schedule \
                         \n\nНа данный момент бот может отправлять только рассписание первых курсов на след. неделю.\
                         Позже появится возможность выбрать курс и расписание какой недели необходимо отправить(текущей или следующей)")