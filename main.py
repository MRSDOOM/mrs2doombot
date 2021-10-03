import os
import telebot

bot = telebot.TeleBot("1974606791:AAGZ2NwYy0H82WCzRx6mUgLUhcH52_kwYUE")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I am Mrs new doom bot")

@bot.message_handler(commads=["how"])
def send_message(message):
    bot.send_message(message, "htps://youtube.com/c/UvinduBro")

bot.polling()

