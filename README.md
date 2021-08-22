# Clickcounter
Урок № 2 модуля "API веб-сервисов" от devman.

## Описание

Квазисчётчик кликов по ссылкам.


### Особенности

* Для начала работы требует:
  * [регистрации](https://bit.ly/),
  * получения [токена](https://bitly.com/a/oauth_apps).
* Исходя из ввода от пользователя:
  * формирует битлинк из _long URL_.
  * считает кол-во переходов по битлинку,
    + подсчёт управляется query-параметрами [метода](https://dev.bitly.com/api-reference#getClicksSummaryForBitlink).
* обрабатывает исключения при некорректном вводе _long URL_* или _bitlink_* от пользователя.




Определение понятий см. [тут](https://github.com/Padking/clickcounter/wiki).
