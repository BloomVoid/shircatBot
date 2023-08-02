from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


back_menus = InlineKeyboardMarkup()
back = InlineKeyboardButton(text='🔙',callback_data='start')
back_menus.row(back)