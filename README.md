# Создание backenda с использованием Django Rest Framework

## Документация по проекту
### Для запуска проекта необходимо:

Активировать виртуальное окружение:
Создать:

```bash
python -m venv venv
```

Активировать:

```bash
\venv\Script\activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Вам необходимо будет создать базу в postgres и прогнать миграции:

```bash
python manage.py migrate
```

Выполнить команду:

```bash
python manage.py runserver
```

Деактивировать виртуальное окружение:

```bash
deactivate
```