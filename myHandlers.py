import telegram
from telegram.ext import Updater, Dispatcher
from telegram.ext import Handler, CommandHandler, MessageHandler, BaseFilter, Filters
from telegram import MessageEntity
import os

adminId = 522799029





#startHandles
def startHandle(bot, update):

  userId = update.message.chat_id

  #for admin
  if userId == adminId:
    #print("Here's an admin")
    buttons = [["Add Admin", "Reply Messages"]]
    keyboard = telegram.ReplyKeyboardMarkup(buttons,resize_keyboard=True)
    bot.send_message(chat_id=int(userId), text="Hello Admin, \n What do you wanna do?", reply_markup=keyboard)

  #for subscriber
  else:
    #print("He's not an admin")
    #checkReg = open(users.txt)
    openreg = open('users.txt', 'r')
    users = openreg.readlines()

    #for registered user
    if str(userId) in users:
      #print("A user here")
      bot.send_message(chat_id=update.message.chat_id, text="You already started the bot. \n You can  send your message to the admin")

    #for new user
    else:
      openreg.close()
      #print(users)
      bot.send_message(chat_id=update.message.chat_id, text="You're welcome to Dreamberg")
      regUser = open('users.txt', 'a+')
      regUser.write('\n' + str(userId))
      regUser.close()





#subMsgHandlers
def subMsgHandle(bot, update):
  userId = update.message.chat_id
  bot.send_message(chat_id=userId, text="Your message has been recieved")
  print(update.message.text)
  bot.forward_message(chat_id=int(adminId), from_chat_id=update.message.chat_id, message_id=update.message.message_id)




#admin keyboard handles
def adminHandle(bot, update):
  #print(update.message.text)
  userId = update.message.chat_id
  if userId == adminId and update.message.text == "Add Admin":
    bot.send_message(chat_id=adminId, text="This feature has not been activated")  

  elif userId == adminId and update.message.text == "Reply Messages":
    bot.send_message(chat_id=adminId, text="Please tap the message you wanna reply and reply it")

  elif userId != adminId:
    bot.send_message(chat_id=update.message.chat_id, text="You are nou authorized to make this request")




#admin reply handles
def replyMsgHandle(bot, update):
  userId = update.message.chat_id
  if userId == adminId:
    bot.send_message(chat_id=adminId, text="Reply sent")
    #print(update.message.reply_to_message.forward_from.id)
    bot.send_message(chat_id=update.message.reply_to_message.forward_from.id, text=update.message.text)

  else:
    bot.send_message(chat_id=userId, text="You're not an admin")
