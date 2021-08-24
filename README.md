# Clickcounter
Урок № 2 модуля "API веб-сервисов" от devman.

## Описание

Квазисчётчик кликов по ссылкам.


### Особенности

* Для начала работы требует:
  * [регистрации](https://bit.ly/),
  * получения [токена](https://bitly.com/a/oauth_apps).
* Исходя из вида _long URL_, передаваемого пользователем в качестве параметра скрипта:
  * формирует битлинк,
  * считает кол-во переходов по битлинку,
    + подсчёт управляется query-параметрами [метода](https://dev.bitly.com/api-reference#getClicksSummaryForBitlink).
* обрабатывает исключения при некорректном вводе _long URL_* или _bitlink_* от пользователя.


### Используемые технологии

* [requests](https://docs.python-requests.org/en/master/)

### Требования к окружения

* Python 3.7 и выше,
* Linux/Windows.

### Установка

```bash
git clone https://github.com/Padking/clickcounter.git  # клонирование проекта
cd clickcounter
```
`mkvirtualenv -p` <path_to_python> <virtualenv's_name>  # создание каталога виртуального окружения (ВО)**

`setvirtualenvproject` <virtualenv's_path> <project's_path>  # связывание каталогов ВО и проекта
```bash
pip install -r requirements.txt # установка зависимостей
```
`python click_informer.py <link>`  # запуск скрипта

### Пример запуска

```bash
$ python click_informer.py https://hctraktor.org/team/players/
Битлинк bit.ly/3swekD9
```
```bash
$ python click_informer.py https://bit.ly/3swekD9
По вашей ссылке прошли: 6 раз(а)
```


\* определение понятий см. [тут](https://github.com/Padking/clickcounter/wiki).

\** с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
