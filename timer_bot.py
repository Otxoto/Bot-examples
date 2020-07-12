# *- coding: utf-8 -*-

#This script shows how to program a timer in a secondary thread.
#this timer can be used to execute tasks from time to time or at a specific time

import telebot
import time, datetime
import threading

import db_functions

bot = telebot.TeleBot('TOKEN')


chat_id = None

def tic_tac():

    i = 0

    while True:

        this_moment = datetime.datetime.now()

        #Executes each 60 secondss
        if ((i % 60) == 0):
            if chat_id:
                bot.send_message(chat_id, "Hello! How are you?")

        #Check if it is 12:00:00; if it is true sends the message
        if this_moment.hour == 21 and this_moment.minute == 30 and this_moment.second == 0:
            if chat_id:
                bot.send_message(chat_id, "It is the noon!")

        i += 1
        time.sleep(1)

#Needs to be started to know the chat id to send messages
@bot.message_handler(commands=['start'])
def save_chat_id(message):
    global chat_id
    chat_id = message.chat.id 
    bot.send_message(chat_id, 'I got it', reply_to_message_id=message.message_id)



timThr = threading.Thread(target=tic_tac)
timThr.start()
bot.polling(none_stop=True)
