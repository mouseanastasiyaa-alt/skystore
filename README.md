# Skystore

Интернет-магазин плагинов, примеров кода и готовых решений.

## 📋 Описание

**Skystore** — онлайн-каталог, где можно продавать и покупать:

- сервисы рассылок;
- Telegram-ботов;
- полезные утилиты;
- веб-приложения;
- микросервисы.

На текущем этапе реализованы главная страница (каталог) и страница контактов
с формой обратной связи.

## 🛠 Стек технологий

- **Python** 3.10+
- **Django** 6.1
- **Bootstrap** 5.3 (CDN)
- **SQLite** (база данных по умолчанию)
- **Git / GitHub** (GitFlow)

## 📁 Структура проекта

```
skystore/
├── .gitignore
├── README.md
├── requirements.txt
├── manage.py
├── config/                    # настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── catalog/                   # приложение каталога
    ├── urls.py
    ├── views.py
    └── templates/catalog/
        ├── home.html
        └── contacts.html
```

## ⚙️ Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/mouseanastasiyaa-alt/skystore.git
cd skystore
```

### 2. Создать и активировать виртуальное окружение

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Применить миграции

```bash
python manage.py migrate
```

### 5. Запустить сервер разработки

```bash
python manage.py runserver
```

Проект будет доступен по адресу: **http://127.0.0.1:8000/**

## 🌐 Маршруты

| URL | Имя | Описание |
|---|---|---|
| `/` | `catalog:home` | Главная страница — каталог |
| `/contacts/` | `catalog:contacts` | Страница контактов с формой обратной связи |
| `/admin/` | — | Админ-панель Django |

## ✅ Что реализовано

- Django-проект Skystore, приложение `catalog`
- Приложение зарегистрировано в `INSTALLED_APPS`
- Маршрутизация через `include`
- Шаблоны `home.html` и `contacts.html` со стилями Bootstrap 5
- Контроллеры `home` и `contacts` через функцию `render`
- Форма обратной связи с выводом сообщения об успешной отправке
- `.gitignore` настроен (`.idea`, `.venv`, `__pycache__`, `db.sqlite3`)
- `requirements.txt` с зависимостями

## 👤 Автор

**Анастасия Чеснокова**
Учебный проект в рамках курса по Django.

## 📄 Лицензия

Проект создан в учебных целях.