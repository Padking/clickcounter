# Clickcounter
Урок № 2 модуля "API веб-сервисов" от devman.

## Описание

Квазисчётчик кликов по ссылкам.


### Особенности

* Для начала работы требует:
  * [регистрации](https://bit.ly/),
  * получения [токена](https://bitly.com/a/oauth_apps).
* Исходя из вида [long URL](https://github.com/Padking/clickcounter/wiki), передаваемого пользователем в качестве параметра скрипта:
  * формирует битлинк,
  * считает кол-во переходов по битлинку,
    + подсчёт управляется query-параметрами [метода](https://dev.bitly.com/api-reference#getClicksSummaryForBitlink).
* обрабатывает исключения при некорректном вводе long URL или [bitlink](https://github.com/Padking/clickcounter/wiki) от пользователя.


### Требования к окружения

* Python 3.7 и выше,
* Linux/Windows.
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно указать их в файле `.env`.
Передача значений ПеО происходит с использованием [python-dotenv](https://pypi.org/project/python-dotenv/).

#### Параметры проекта

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`BITLY_GENERIC_ACCESS_TOKEN`| Токен сервиса [bitly](https://bit.ly/) | - |

### Установка

- Клонирование проекта,
- создание каталога виртуального окружения (ВО)*,
-  связывание каталогов ВО и проекта,
-  установка зависимостей,
-  запуск скрипта:
```bash
git clone https://github.com/Padking/clickcounter.git
cd clickcounter
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements.txt
python main.py <link>
```

\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html).


### Пример запуска

```bash
$ python main.py https://hctraktor.org/team/players/
Битлинк bit.ly/3swekD9
```
```bash
$ python main.py https://bit.ly/3swekD9
По вашей ссылке прошли: 6 раз(а)
```
