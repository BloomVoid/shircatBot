from aiogram import types
import inline_menu.back_menu
async def news_handler(dp):
    @dp.callback_query_handler(text_startswith='news')
    async def search(call: types.CallbackQuery):
        text = f'''
@{call.message.chat.first_name} вы вы выбрали каталог новости 🗞️ 
К сожалению на данный момент данный каталог пуст но в скором времени он пополнится различной информацией 🏜️
В данном каталоге буду такие форматы как 
😈 Сливы  мошенников 
🔥 базы данных 
🔍 обновлённый поиск 
🧿 выбор языка 
И прочее ❤️ 
Все будет делаться для будущего комфортного использования ! 🌵
'''
        await call.answer()
        await call.message.edit_text(text,reply_markup=inline_menu.back_menu.back_menus)
        news_handler(dp)