import telegram
from telegram.ext import Updater, Dispatcher
from telegram.ext import Handler, CommandHandler
from telegram import MessageEntity
from telegram import User

bot = telegram.Bot(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
updater = Updater(token="666720872:AAF-px3ihfHBXSscVnehO_hB7NIVNn7q6QY")
dispatcher = updater.dispatcher


#start handler
def startHandle(bot, update):
  userId = int(update.message.chat_id)
  checkRank = open('admins.txt', 'r+')
  admins = checkRank.readlines()
  openReg = open('users.txt', 'r+')
  users = openReg.readlines()
  if userId in users:
    bot.send_message(chat_id=update.message.chat_id, text="You already started the bot. \n You can  send your message to the admin")
    openReg.close()
  elif userId not in admins:
      regUser = open('users.txt', 'a+')
      regUser.write(userId)
      regUser.close()
      bot.send_message(chat_id=update.message.chat_id, text="You're welcome to Dreamberg")
  
  elif userId in admins:
      buttons = [["Add Admin", "Reply Messages"]]
      keyboard = telegram.ReplyKeyboardMarkup(buttons,resize_keyboard=True)
      bot.send_message(chat_id=int(userId), text="Hello Admin, \n What do you wanna do?", reply_markup=keyboard)
      checkRank.close()

  
  
#messages handlers

def subMsgHandle(bot, update):
  userId = str(update.message.chat_id)
  openReg = open('admins.txt', 'r+')
  admins = openReg.readlines()

  #Check Admin Commands
  if userId in admins:
    msg = update.message.text    


    #ad admin Command
    if msg == "Add Admin":
      bot.send_message(chat_id=int(userId), text="admin will be added later")



#reply message
    elif "Re:" in msg:
      getRec = open('replySession.txt', 'r')
      recz = getRec.readlines()
      rec = (recz[0])
      bot.send_message(chat_id=int(rec), text=msg)
      repSessionFile.close()
       

    #reply messages command
    elif msg == "Reply Messages":
      bot.send_message(chat_id=int(userId), text="We'll reply messages later")
    

    
    
    #reply message request
    elif update.message.forward_from.id is not None:
      repSessionFile = open('replySession.txt', 'w+')
      repSessionFile.write(str(update.message.forward_from.id))
      repSessionFile.close()
      bot.send_message(userId, text="now send your message")


    #catch Error
    else:
      bot.send_message(chat_id=int(userId), text="I don't understand your query please try again")
      print(update.message.forward_from.id)


    

  #subscriber reply
  else:
    bot.send_message(chat_id=update.message.chat_id, text="Message recieved")
    for admin in admins:
      bot.forward_message(chat_id=int(admin), from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    print("message forwarded")

