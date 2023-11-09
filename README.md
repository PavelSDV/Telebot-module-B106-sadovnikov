# skillfactory-module-B106-sadovnikov-Telebot

---------------------
Задание

Ваше задание: написать telegram-бота, в котором будет реализован следующий функционал:

Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).

При написании бота необходимо использовать библиотеку pytelegrambotapi.

Человек должен отправить сообщение боту в виде <имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>.

При вводе команды /start или /help пользователю выводятся инструкции по применению бота.


При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.

Для взятия курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests.

Для парсинга полученных ответов использовать библиотеку JSON.

При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.

Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.

Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента: имя валюты, цену на которую надо узнать, — base, имя валюты, цену в которой надо узнать, — quote, количество переводимой валюты — amount и возвращает нужную сумму в валюте.

Токен telegramm-бота хранить в специальном конфиге (можно использовать .py файл).

Все классы спрятать в файле extensions.py.

-------------------------
Итоговая оценка

27
из 28
баллов

1
Возврат цены валюты при отправке сообщения пользователем
Отлично
4 балла

2
Дополнительные библиотеки
Отлично
3 балла

3
Ввод команды /values
Отлично
2 балла

4
Запросы к стороннему API
Хорошо
2 балла

5
Библиотека JSON
Отлично
2 балла

6
Исключение APIException
Отлично
5 балла

7
Дополнительные структуры данных (класс или функция)
Отлично
3 балла

8
Токен телеграмм-бота
Отлично
3 балла

9
Хранение в файле extensions.py
Отлично
3 балла

Добрый день! Работа оценена максимальными баллами по каждому критерию, за исключением использования API ресурса, отличного от https://exchangeratesapi.io/.
Код удовлетворяет всем правилам и стандартам PEP8, структура файлов выполнена верно, переменные и функции имеют корректные имена, вычисление при работе с API выполнено верно и в нужном файле

В целом все выполнено отлично, продолжайте в том же духе!
Проверку выполнила ментор Попова Екатерина.
Если у вас остались вопросы, вы можете обратиться в канал #module_b10 в Slack