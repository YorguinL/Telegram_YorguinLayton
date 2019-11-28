#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from programaBot import ProgramaBot

TOKEN = '940620192:AAG5K2iDKH_ATTxWmz8iz2a3Ppi-v4srAF8'
bot = telebot.TeleBot(TOKEN)
p = ProgramaBot()
p.idUsuari

@bot.message_handler(commands=['inici'])
def mensaje_bienvenida(message):
	bot.reply_to(message, "Heeeeey! Para jugar utiliza el comando /jugar y si tienes dudas utiliza /ayuda")
	p.idUsuari = message.user.id
@bot.message_handler(commands=['jugar'])
def comenzar_juego(message):
	bot.reply_to(message, "Comencemos! Introduce un número del 0 al 100.")

@bot.message_handler(func=lambda message: True)
def comenzar_juego(message):
	try:
		p.numUsuari=(int(message.text))
		p.comprovar()
		if p.rangValid == True:
			if p.solucio == True:
				bot.send_message('673273081', "L'has endevinat en " + str(p.count) + " intents.")
			else:
				bot.send_message('673273081', "Nmero incorrecte, torna-ho a intentar")
		else:
			bot.send_message('673273081', "Estas fora del rang")
		print message.user.id
		print p.idUsuari
		print p.numUsuari
		print p.nAleatori
	except:
		pass

#bot.send_message('673273081', 'hdp')
bot.polling()
