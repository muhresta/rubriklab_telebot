import telebot
import requests
import datetime

bot.polling(none_stop=True)

@bot.message_handler(commands=["start"])
def start_command(message):
    bot.send_message(
        message.chat.id,
        "Hello, Rubrik Bot Here!\n" +
        "To get report press /report.\n" +
        "To create SLA press /createSLA."
    )
    
@bot.message_handler(commands=["report"])
def report_command(message):
    keyboard = telebot.types.InLineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Task Status', callback_data="get-Task")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Storage Status', callback_data="get-Storage")
    )
    
    bot.send_message(message.chat.id, "What do you want to?", reply_markup=keyboard)

@bot.message_handler(commands="createSLA")
def createsla_command(message):
    keyboard.row(
        telebot.types.InlineKeyboardButton()
    )