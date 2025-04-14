# 🏆 Reward Platform API

API-платформа для выдачи наград пользователям с отложенным начислением с использованием Django REST Framework, Celery и Redis.

## 🚀 Технологии

- Python 3.9+
- Django 4+
- Django REST Framework
- PostgreSQL
- Celery + Redis
- JWT (Simple JWT)
- Swagger / drf-spectacular

## 📦 Установка



git clone https://github.com/yourname/reward-platform.git

cd reward_platform

py -3.9 -m venv venv

source venv/Scripts/activate

cd backend

docker-compose up

docker-compose exec web python manage.py createsuperuser

Получение токена по http://127.0.0.1:8000/api/token/

Пример:
{
  "username": "bob",
  "password": "123"
}


Вставте access в Authorize в http://127.0.0.1:8000/swagger/




