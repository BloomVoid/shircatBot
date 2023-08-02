import lib.bucket
import security.config
from concurrent.futures.thread import _shutdown
from handler.handler_start import procces_start
from handler.handler_news import news_handler
from handler.handler_profile import handler_profiles
from handler.user_token import token_message
from handler.handler_report import handler_reports
from handler.handler_yslyg import handler_yslygi


bot = lib.bucket.Bot(token=security.config.TOKEN)
storage = lib.bucket.MemoryStorage()
main = lib.bucket.Dispatcher(bot, storage=storage)

lib.bucket.logging.basicConfig(level=lib.bucket.logging.INFO)
  
async def on_startup(dp):
    await procces_start(dp)
    await news_handler(dp)
    await handler_profiles(dp)
    await token_message(dp)
    await handler_reports(dp)
    await handler_yslygi(dp)

 
if __name__ == "__main__":
    lib.bucket.executor.start_polling(main, on_startup=on_startup, on_shutdown=_shutdown)
