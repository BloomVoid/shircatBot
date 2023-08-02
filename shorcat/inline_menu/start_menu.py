from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu_start = InlineKeyboardMarkup()
profile = InlineKeyboardButton(text='🤵 Профиль ',callback_data='profile')
search = InlineKeyboardButton(text='🔍 Поиск ',url='https://t.me/+pfdtdYapkmMxNTVh')
news = InlineKeyboardButton(text='📋 Новости',callback_data='news')
yslyga = InlineKeyboardButton(text='💰 Услуги',callback_data='yslyga')
report = InlineKeyboardButton(text='😈 Репорт ',callback_data='report')
menu_start.row(profile,yslyga,news)
menu_start.row(report,search)