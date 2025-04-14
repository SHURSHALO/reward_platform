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

Переименуйте .env.example в .env

py -3.9 -m venv venv

source venv/Scripts/activate

cd backend

docker-compose up

Соберем статику
docker-compose exec web python manage.py collectstatic --noinput

Создадим суперюзера например
docker-compose exec web python manage.py shell

Вводим построчно
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='admin')
user.set_password('mypassword')  # Задай нужный тебе пароль
user.save()
После этого выходи из shell:
exit()

Получение токена по http://127.0.0.1:8000/api/token/

Пример:
{
  "username": "bob",
  "password": "123"
}


Вставте access в Authorize в http://127.0.0.1:8000/swagger/




