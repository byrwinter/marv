import telegram
from telegram.ext import Updater, Dispatcher, CommandHandler, Handler
import os



bot = telegram.Bot(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
updater = Updater(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
dispatcher = updater.dispatcher


TOKEN = "666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY"
PORT = int(os.environ.get('PORT', '8443'))


def echo(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="update.message.text")



startHandler = CommandHandler('start', echo)
dispatcher.add_handler(startHandler)



# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://initot.herokuapp.com/" + TOKEN)
updater.idle()

