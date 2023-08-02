from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


usluga_menu = InlineKeyboardMarkup()
doxbin = InlineKeyboardButton(text='😈 Докс',url='http://t.me/YavnoUse')
reklama = InlineKeyboardButton(text='🧑‍💻 Реклама ',url='http://t.me/YavnoUse')
script  = InlineKeyboardButton(text='⚙️ Скрипт ',url='https://t.me/+s6tOYZugEfFjMDM6')
Bot = InlineKeyboardButton(text='🎃 ТгБот',url='https://t.me/+s6tOYZugEfFjMDM6')
back = InlineKeyboardButton(text='🔙',callback_data='start')
usluga_menu.row(doxbin,reklama )
usluga_menu.row(script,Bot)
usluga_menu.row(back)