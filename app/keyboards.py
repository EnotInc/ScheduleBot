from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Расписание на эту неделю")],
    [KeyboardButton(text="Расписание на след. неделю")]
], resize_keyboard=True, input_field_placeholder="Выберите один из пунктов в меню")
