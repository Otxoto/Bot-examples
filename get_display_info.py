# *- coding: utf-8 -*-


import mysql_script

import telebot
from telebot import util, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot_id = 9
bot = telebot.TeleBot(mysql_script.dame_token(bot_id))

#Get and display information about command sender
@bot.message_handler(commands=['me'])
def send_user_data(message):
    user = message.from_user
    text = 'User:\n<code>{0}</code>'.format(user)
    #if the command has sent in a group get and display status and other information
    #about the command sender
    if message.chat.id < 0:
        chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
        text += '\n\nChat member:\n<code>{0}</code>'.format(chat_member)
    bot.send_message(message.chat.id, text, parse_mode='HTML')

#Get and display information about the bot
@bot.message_handler(commands=['bot'])
def send_getme(message):    
    me = bot.get_me()
    text = '<code>' + str(me) + '</code>'
    bot.send_message(message.chat.id, text, parse_mode='HTML')

#get and display information about the chat
@bot.message_handler(commands=['chat'])
def send_chat_data(message):
    chat = message.chat
    text = '<code>' + str(chat) + '</code>'
    bot.send_message(message.chat.id, text, parse_mode='HTML')
    

bot.polling(none_stop=True)