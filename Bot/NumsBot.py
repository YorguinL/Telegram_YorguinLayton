#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot

TOKEN = '940620192:AAG5K2iDKH_ATTxWmz8iz2a3Ppi-v4srAF8'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Heeeey!")
	bot.send_message('673273081', 'hdp')

@bot.message_handler ( func = lambda  m : True )
def  echo_all(message):
    print(message.chat.id)
    bot.reply_to(message, message.text)

bot.send_message('673273081', 'hdp')

bot.polling()
