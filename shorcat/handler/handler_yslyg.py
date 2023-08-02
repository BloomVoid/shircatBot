from aiogram import types
import inline_menu.yslyga_menu

async def handler_yslygi(dp):
    @dp.callback_query_handler(text_startswith='yslyga')
    async def search(call: types.CallbackQuery):
        await call.answer()
        text = f'''
@{call.message.chat.first_name} 🧿 вы выбрали каталог услуги 💰
В данном каталоге вы можете заказать такие вещи как 
Если вас что нибудь заинтересовало будьте добры 🧑‍💻 получить токен и отправить свои пожелания в репорт 😁
'''
        await call.message.edit_text(text,reply_markup=inline_menu.yslyga_menu.usluga_menu)
        handler_yslygi(dp)
