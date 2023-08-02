import lib.bucket
from aiogram import types
 

async def token_message(dp):
    @dp.message_handler(commands=("token"))
    async def generate_token(message: types.Message, state: lib.bucket.FSMContext):
        data = await state.get_data()
        if "token" in data:
            token = data["token"]
            await message.answer(f"@{message.chat.first_name} 🧿 ваш токен уже был сгенерирован и выдан вам 🤵Для того чтоб его увидеть вам нужно  выбрать каталог 🔜 [🤵 Профиль ]")
        else:
            token = ''.join(lib.bucket.random.choices(lib.bucket.string.ascii_uppercase + lib.bucket.string.digits, k=10))
            await state.update_data(token=token)
            await message.answer(text= f"@{message.chat.first_name} 🧿 ваш токен сгенерирован 🔜 {token}")
    token_message(dp) 
        