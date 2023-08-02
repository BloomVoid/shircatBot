from aiogram import types
import image.image_start
import inline_menu.start_menu

async def procces_start(dp):
    @dp.message_handler(commands='start')
    async def start(message: types.Message):
        chat = message.chat.id
        text = '''
Добро пожаловать в бота поддержку канала Shortac 
Ссылка на канал: http://t.me/+-ROyI-aK7M4wMTMy 🔚
В данном боте вы сможете проверить список мошенников и так же указать и отослать репорт на мошенника 🔍
📃 Бот абсолютно бесплатный и не включает на данный момент в себя никаких подписок и привилегий 📃 
Для того чтоб оставить заявку на репорт нажмите на кнопку [ 😈 Репорт  ] 🧿
Так же хотим пожелать вам приятного пользования и хорошего настроения 🔥
'''
        await dp.bot.send_photo(chat,image.image_start.start_image)
        await message.answer(text,reply_markup=inline_menu.start_menu.menu_start)


    @dp.callback_query_handler(text_startswith='start')
    async def search(call: types.CallbackQuery):
        await call.answer()
        text = '''
Добро пожаловать в бота поддержку канала Shortac 
Ссылка на канал: http://t.me/+-ROyI-aK7M4wMTMy 🔚
В данном боте вы сможете проверить список мошенников и так же указать и отослать репорт на мошенника 🔍
📃 Бот абсолютно бесплатный и не включает на данный момент в себя никаких подписок и привилегий 📃 
Для того чтоб оставить заявку на репорт нажмите на кнопку [ 😈 Репорт  ] 🧿
Так же хотим пожелать вам приятного пользования и хорошего настроения 🔥
'''
        await call.message.edit_text(text,reply_markup=inline_menu.start_menu.menu_start)
    
    procces_start(dp)