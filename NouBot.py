#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot

TOKEN = '940620192:AAG5K2iDKH_ATTxWmz8iz2a3Ppi-v4srAF8'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Heeeey!")

bot.polling()
