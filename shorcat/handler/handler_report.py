from aiogram import types
import inline_menu.back_menu
import lib.bucket

async def handler_reports(dp):
    @dp.callback_query_handler(text_startswith='report')
    async def search(call: types.CallbackQuery):
        await call.answer()
        text = f'''
@{call.message.chat.first_name} 🧿 вы выбивали каталог [😈 Репорт ]
Правила заявки 📝
• Сообщение 
• Ссылка с документами ( телеграмм чат - канал 📃 в котором есть доказательство на мошенничество либо же другое злокачественно действие 🤹‍♀️ )
Если вы ознакомились с правилами 📝
Тогда мы можете оставить свою заявку написав ее боту и бот автоматически перешлет ее к нам в базу данных 🎃
'''
        await call.message.edit_text(text,reply_markup=inline_menu.back_menu.back_menus)


    @dp.message_handler()
    async def handle_message(message: types.Message, state: lib.bucket.FSMContext):
        data = await state.get_data()
        if "token" in data:
            token = data["token"]
            forwarded_message = f'''
Пользователь: {message.chat.username}
Айди: {message.chat.id} 
Имя: {message.chat.first_name} 
Токен пользователя: {token}
оставил заявку:\n\n{message.text}            
            
            
            '''
            await dp.bot.send_message(chat_id=-1001609160351, text=forwarded_message)
        else:
            chat = message.chat.id
            await dp.bot.send_message(chat,text='😈 ваша заявка не может быть принята так как вы не получили токен 😈')

    

        handler_reports(dp)