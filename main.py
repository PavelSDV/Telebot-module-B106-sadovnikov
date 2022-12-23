import telebot
import requests
import json

TOKEN = '5944761623:AAFCN-nH4GqOltTZ4tmScVUdutzLn7_oPKw'

bot = telebot.TeleBot(TOKEN)

keys = {
    'рубль': 'RUB',
    'евро': 'EUR',
    'доллар': 'USD',
}

class ConvertionException(Exception):
    pass


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
        raise ConvertionException('Слишком много параметров.')

    quote, base, amount = values

    if quote == base:
        raise ConvertionException(f'Введена одинаковая валюта {base}')

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f'Не удалось обработать валюту {quote}')

    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionException(f'Не удалось обработать валюту {base}')

    try:
        amount = float(amount)
    except ValueError:
        raise ConvertionException(f'Не удалось обработать количество {amount}')


    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)