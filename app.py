import telegram
from telegram.ext import Updater, Dispatcher
from telegram.ext import Handler, CommandHandler, MessageHandler, BaseFilter, Filters
from telegram import MessageEntity
from myHandlers import *


bot = telegram.Bot(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
updater = Updater(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
dispatcher = updater.dispatcher



startHandler = CommandHandler('start', startHandle)
dispatcher.add_handler(startHandler)

subMsgHandler = MessageHandler(Filters.text, subMsgHandle)
dispatcher.add_handler(subMsgHandler)


updater.start_polling()
