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
import logging, settings, ephem, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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
    planet_name = update.message.text.split()[1]
    current_date = datetime.datetime.now()
    if planet_name == 'Mars':
        planet_date = ephem.Mars(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    elif planet_name == 'Mercury':
        planet_date = ephem.Mercury(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    elif planet_name == 'Jupiter':
        planet_date = ephem.Jupiter(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    elif planet_name == 'Neptune':
        planet_date = ephem.Neptune(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    elif planet_name == 'Venus':
        planet_date = ephem.Venus(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    elif planet_name == 'Saturn':
        planet_date = ephem.Saturn(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    elif planet_name == 'Uranus':
        planet_date = ephem.Uranus(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    elif planet_name == 'Moon':
        planet_date = ephem.Moon(current_date)
        update.message.reply_text(f'{planet_name} now in {ephem.constellation(planet_date)[1]} constellation')
    else:
        update.message.reply_text("I know nothing about this planet")
 

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