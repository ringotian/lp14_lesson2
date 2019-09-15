"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.
"""
import logging, settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ephem import *

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def check_constellation(bot, update):
    planet_name = date.message.text.split()[1]
    print(planet_name)
    year = '2019'
    if planet_name == 'Mars':
        planet_date = Mars(year)
    elif planet_name == 'Moon':
        planet_date = Moon(year)
    elif planet_name == 'Mercury':
        planet_date = Mercury(year)
    elif planet_name == 'Jupiter':
        planet_date = Jupiter(year)
    elif planet_name == 'Neptune':
        planet_date = Neptune(year)
    elif planet_name == 'Earth':
        planet_date = Earth(year)
    elif planet_name == 'Venus':
        planet_date = Venus(year)
    elif planet_name == 'Saturn':
        planet_date = Saturn(year)
    elif planet_name == 'Uranus':
        planet_date = Uranus(year)
    text_to_be_replied = constellation(planet_date)[1]
    update.message.reply_text(text_to_be_replied)    

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", check_constellation))

    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()