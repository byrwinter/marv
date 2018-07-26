import telegram
from telegram.ext import Updater, Dispatcher, CommandHandler, Handler
import os
from telegram.ext import  MessageHandler, BaseFilter, Filters
from telegram import MessageEntity
from myHandlers import *


bot = telegram.Bot(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
updater = Updater(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
dispatcher = updater.dispatcher


TOKEN = "666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY"
PORT = int(os.environ.get('PORT', '8443'))


bot = telegram.Bot(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
updater = Updater(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
dispatcher = updater.dispatcher

startHandler = CommandHandler('start', startHandle)
dispatcher.add_handler(startHandler)


#add admin filter
class add_filter(BaseFilter):
    def filter(self, message):
        return 'Add Admin' in message.text

addFilter = add_filter()

#add admin handler
addHandler = MessageHandler(addFilter, adminHandle)
dispatcher.add_handler(addHandler)



#reply messages filter
class rep_filter(BaseFilter):
    def filter(self, message):
        return 'Reply Messages' in message.text

repFilter = rep_filter()

#reply messages handler
repHandler = MessageHandler(repFilter, adminHandle)
dispatcher.add_handler(repHandler)

#reply foward hander
replyMsgHandler = MessageHandler(Filters.reply, replyMsgHandle)
dispatcher.add_handler(replyMsgHandler)

#subMessages handler
subMsgHandler = MessageHandler(Filters.text, subMsgHandle)
dispatcher.add_handler(subMsgHandler)





# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://initot.herokuapp.com/" + TOKEN)
updater.idle()


