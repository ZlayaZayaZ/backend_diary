# Создание backenda с использованием Django Rest Framework

## Документация по проекту
### Для запуска проекта необходимо:

#### Активировать виртуальное окружение:

Создать:

```bash
python -m venv venv
```

Активировать:

```bash
venv\Scripts\activate
```

#### Установить зависимости:

```bash
pip install -r requirements.txt
```

#### Cоздать базу в postgres и прогнать миграции:

```bash
python manage.py migrate
python manage.py makemigrations
```

#### Выполнить команду:

```bash
python manage.py runserver
```

#### Деактивировать виртуальное окружение:

```bash
deactivate
```