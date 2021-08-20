# Clickcounter
Урок № 2 модуля "API веб-сервисов" от devman

## Описание

Псевдосчётчик кликов по ссылкам


### Особенности

* Исходя из ввода от пользователя:
  * формирует битлинк из `long URL`
  * считает кол-во переходов по битлинку
    + подсчёт управляется query-параметрами [метода](https://dev.bitly.com/api-reference#getClicksSummaryForBitlink)
* обрабатывает исключения при некорректном вводе _long URL_ или _bitlink_* от пользователя




* Определение понятий см. [тут](https://github.com/Padking/clickcounter/wiki)
