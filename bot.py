import schedule
import requests
import telebot
import time
from threading import Thread

tg_token = '8138804444:AAGRDgF0oB9CY11YAlroAeQ1652t1SmsvOU'
bot = telebot.TeleBot(tg_token)


def get_weather(message):
    try:
        params = {
            '?0': '',
            'lang': 'en',
            '?M': '',
        }
        weather = requests.get(f'https://wttr.in/{message.text}.png', params=params)
        with open('weather.png', 'wb') as image:
            image.write(weather.content)
        bot.send_photo(message.chat.id, open('weather.png', 'rb'))
    except:
        bot.send_message(message.chat.id, "Couldn't get weather data")


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


Thread(target=run_schedule, daemon=True).start()


@bot.message_handler(commands=['start'])
def start_message(message):
    city = bot.send_message(message.chat.id, 'Send me your city')
    bot.register_next_step_handler(city, get_period)


def get_period(message):
    city = message.text
    period = bot.send_message(message.chat.id, 'How often (in minutes) should I send weather?')
    bot.register_next_step_handler(period, lambda m: setup_schedule(m, city))


def setup_schedule(message, city):
    try:
        minutes = int(message.text)
        schedule.every(minutes).minutes.do(lambda: get_weather_message(city, message.chat.id))
        bot.send_message(message.chat.id, f"Will send weather for {city} every {minutes} minutes")
    except:
        bot.send_message(message.chat.id, "Please enter a valid number")


def get_weather_message(city, chat_id):
    fake_message = type('', (), {'text': city, 'chat': type('', (), {'id': chat_id})})()
    get_weather(fake_message)


bot.infinity_polling()