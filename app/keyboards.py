from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Расписание на эту неделю")],
    [KeyboardButton(text="Расписание на след. неделю")]
], resize_keyboard=True, input_field_placeholder="Выберите неделю")

course_this = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й курс', callback_data='first_this')],
    [InlineKeyboardButton(text='2-й курс', callback_data='second_this')],
    [InlineKeyboardButton(text='3-й курс', callback_data='third_this')],
    [InlineKeyboardButton(text='4/5-й курс', callback_data='last_this')]
])

course_next = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1-й курс', callback_data='first_next')],
    [InlineKeyboardButton(text='2-й курс', callback_data='second_next')],
    [InlineKeyboardButton(text='3-й курс', callback_data='third_next')],
    [InlineKeyboardButton(text='4/5-й курс', callback_data='last_next')]
])