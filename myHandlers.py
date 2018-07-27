import telegram
from telegram.ext import Updater, Dispatcher
from telegram.ext import Handler, CommandHandler, MessageHandler, BaseFilter, Filters
from telegram import MessageEntity
from emoji import emojize
import os


#569482800
adminId = 522799029

 #print(emoji.emojize('Python is :thumbs_up:'))
#emoji = emoji
#emojis

smile = emojize(':smile:', use_aliases=True)
wave = emojize(':wave:', use_aliases=True)
thumbsup = emojize(':thumbsup:', use_aliases=True)
confused = emojize(':confused:', use_aliases=True)
perfecto = emojize(':ok_hand:', use_aliases=True)




#startHandles
def startHandle(bot, update):

  userId = update.message.chat_id

  #for admin
  if userId == adminId:
    #print("Here's an admin")
    buttons = [["Add Admin", "Reply Messages"]]
    keyboard = telegram.ReplyKeyboardMarkup(buttons,resize_keyboard=True)
    bot.send_message(chat_id=int(userId), text="Hello Admin" + smile + "\n What do you wanna do?", reply_markup=keyboard)

  #for subscriber
  else:
    #print("He's not an admin")
    #checkReg = open(users.txt)
    openreg = open('users.txt', 'r')
    users = openreg.readlines()

    #for registered user
    if str(userId) in users:
      #print("A user here")
      bot.send_message(chat_id=update.message.chat_id, text=confused + " You've already started the bot.\nYou can now send your message to the admin " + smile)

    #for new user
    else:
      openreg.close()
      #print(users)
      bot.send_message(chat_id=update.message.chat_id, text="Hello " + smile  + "\nI'm Initot, the official bot for the admins of @marvel_newz. Send any message to them through me.")
      regUser = open('users.txt', 'a+')
      regUser.write('\n' + str(userId))
      regUser.close()





#subMsgHandlers
def subMsgHandle(bot, update):
  userId = update.message.chat_id
  bot.send_message(chat_id=userId, text=perfecto + "\nYour message has been recieved")
  #print(update.message.text)
  bot.forward_message(chat_id=int(adminId), from_chat_id=update.message.chat_id, message_id=update.message.message_id)




#admin keyboard handles
def adminHandle(bot, update):
  #print(update.message.text)
  userId = update.message.chat_id
  if userId == adminId and update.message.text == "Add Admin":
    bot.send_message(chat_id=adminId, text=confused + " This feature has not been activated")  

  elif userId == adminId and update.message.text == "Reply Messages":
    bot.send_message(chat_id=adminId, text=smile + " Please tap the message you wanna reply and reply it")

  elif userId != adminId:
    bot.send_message(chat_id=update.message.chat_id, text="You are not authorized to make this request")




#admin reply handles
def replyMsgHandle(bot, update):
  userId = update.message.chat_id
  if userId == adminId:
    bot.send_message(chat_id=adminId, text=thumbsup + "\nReply sent")
    #print(update.message.reply_to_message.forward_from.id)
    bot.send_message(chat_id=update.message.reply_to_message.forward_from.id, text= wave + " Reply: " + "\n" + update.message.text)

  else:
    bot.send_message(chat_id=userId, text="You're not an admin")
