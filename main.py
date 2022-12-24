#https://t.me/ExchangeTelebot
#name - TelebotExchange

import telebot
from config import keys, TOKEN
from extensions import ConvertionException, Converter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> <количество переводимой валюты> \n \
Увидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(commands=['hello', ])
def welcome(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.username}")

@bot.message_handler(content_types=['voice', ])
def voice_hear(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Слышу голос {message.chat.username}")

@bot.message_handler(content_types=['photo', ])
def say_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Хорошее фото')

@bot.message_handler(content_types=['text', ])
def exchange(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Должно быть три параметра')

    quote, base, amount = values
    total_base = Converter.exchange(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
