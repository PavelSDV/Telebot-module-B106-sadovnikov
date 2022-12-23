import requests
import json

keys = {
    'рубль': 'RUB',
    'евро': 'EUR',
    'доллар': 'USD',
}

class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def exchange(quote: str, base: str, amount: str):
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

        return total_base
