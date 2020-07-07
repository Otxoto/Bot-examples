# *- coding: utf-8 -*-
# This example shows how to use inline buttons and process their calls

import telebot
from telebot import util, types
from telebot import types

TELEGRAM_TOKEN = '<TOKEN>'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def starting_point(message):
    mkup = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton("A", callback_data="A")
    itembtn2 = types.InlineKeyboardButton("B", callback_data="B")
    mkup.add(itembtn1, itembtn2)
    text = "Hello! Choose one option"
    bot.send_message(message.chat.id, text, reply_markup=mkup)


@bot.callback_query_handler(func=lambda call: call.data == 'A')
def a_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton("Back", callback_data="C")
    mkup.add(itembtn1)
    text = "You chose A"
    bot.edit_message_text( text, call.message.chat.id, call.message.message_id, reply_markup=mkup)


@bot.callback_query_handler(func=lambda call: call.data == 'B')
def b_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton("Back", callback_data="C")
    mkup.add(itembtn1)
    text = "You chose B"
    bot.edit_message_text( text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

@bot.callback_query_handler(func=lambda call: call.data == 'C')
def c_choosen(call):
    mkup = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton("A", callback_data="A")
    itembtn2 = types.InlineKeyboardButton("B", callback_data="B")
    mkup.add(itembtn1, itembtn2)
    text = "Hello again! Choose one."
    bot.edit_message_text( text, call.message.chat.id, call.message.message_id, reply_markup=mkup)

bot.polling(none_stop=True)
