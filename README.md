# StatEduBot

Это бот для отслеживания изменения баллов по пробникам ЕГЭ, созданный с использованием aiogram и SQLAlchemy.

![Меню](https://imgur.com/ocYu7BJ)

## Содержание

- [Установка](#установка)
- [Запуск](#запуск)
- [Реализованные функции](#реализованные-функции)
- [Структура проекта](#структура-проекта)
- [Используемые технологии](#используемые-технологии)
- [Комментарий](#комментарий)

## Установка

Для начала клонируйте репозиторий и установите зависимости:

```sh
git clone https://github.com/453254/StatEduBot.git
cd StatEduBot
```

Создайте виртуальное окружение и активируйте его:

```sh
python -m venv venv
.\venv\Scripts\activate  # для Windows
source venv/bin/activate  # для Unix
```

Установите зависимости:

Все необходимые библиотеки для полного запуска:
```sh
requirements.txt
```

## Запуск

Для запуска проекта используйте команду:

```sh
python 

main.py


```

## Реализованные функции

- **Регистрация предметов**: Возможность добавлять и удалять предметы для отслеживания.
- **Запись результатов**: Возможность записывать результаты пробников.
- **Просмотр статистики**: Возможность просматривать статистику по предметам.

## Структура проекта

```
└── 📁StatEduBot
    └── 📁__pycache__
    └── 📁.git
    └── 📁.idea
    └── 📁.venv
    └── 📁app
        └── 📁__pycache__
        └── 📁database
            └── models.py
            └── requests_del.py
            └── requests_register.py
            └── requests_resoult.py
            └── requests_stats.py
            └── requests.py
        └── 📁del_resoult
            └── handlers_del.py
            └── keyboard_del.py
            └── states_del.py
        └── 📁edit_resoult
            └── handlers_resoult.py
            └── keyboards_resoult.py
            └── states_resoult.py
        └── 📁register
            └── add_subjects_register.py
            └── hendlers_register.py
            └── keyboard_register.py
            └── states_register.py
        └── 📁stats
            └── 📁create_graph
                └── generator_graph.py
            └── handlers_stats.py
            └── keyboard_stats.py
            └── states_stats.py
        └── handlers.py
        └── keyboards.py
        └── utils.py
    └── .env
    └── .gitignore
    └── main.py
    └── README.md
    └── requirements.txt
    └── TEST.py
    └── users.db
```

## Используемые технологии

- [aiogram](https://docs.aiogram.dev/en/latest/) - Асинхронный фреймворк для создания Telegram ботов.
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit и ORM для Python.
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Загрузка переменных окружения из .env файла.

## Комментарий

- Здесь ужасная структура, которую следовало бы переделать 🫡
