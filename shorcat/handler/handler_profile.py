from aiogram import types
import lib.bucket
import inline_menu.back_menu

async def handler_profiles(dp):
    @dp.callback_query_handler(text_startswith='profile')
    async def search(call: types.CallbackQuery, state: lib.bucket.FSMContext):
        call.data = await state.get_data()
        token = call.data.get("token", "нет токена")  
        texts = f'''
@{call.message.chat.first_name} 🧿 вы выбрали каталог профиль 🤵 
В данном каталоге вы можете увидеть данные о себе такие как 🏜 
Ваш 🆔: {call.message.chat.id}
Ваше 🙎: {call.message.chat.first_name}
Ваш персональный токен: {token}
Ваш 🧑‍💻: {call.message.chat.username}
🔥 Со времени профиль будет пополняться и будут добавлены новые функции 🌵
⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️⚙️
Так же не забывайте проверять канал [ 📋 новости ] 🧑‍💻 и другие каналы 🎃
🔜 так же если у вас нету персонального токена вам нужно нажать /token 🔥 
Токен предназначен для того чтоб мы знали кто оставляет заявки на репорт 😈
'''
        await call.message.edit_text(texts, reply_markup=inline_menu.back_menu.back_menus)
        handler_profiles(dp) 