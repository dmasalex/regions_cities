# regions_cities
Тестовое задание на должность Python Backend Developer

Разработать REST-API для управления списком регионов и городов, которые в них входят.
Необходимо реализовать выборку регионов, выборку городов по региону, CRUD для городов и регионов.
Для неавторизованного пользователя должны быть доступны только выборки данных.
Для проверки нужно создать в базе 1-2 пользователей, управление их записями через API не предполагается.
В качестве БД рекомендуется использовать postgresql, Flask - как фреймворк для создания веб-сервера.

1. Установка виртуального окружения и зависимосей:
pip install Flask
pip install Flask-SQLAlchemy
pip install psycopg2
pip install Flask-WTF
pip install Flask-Admin
pip install Flask-Security
pip install email_validator
pip install login
pip install bcrypt

2. Создания БД и пользователя к ней:
sudo psql -U postgres
CREATE DATABASE regcity;
CREATE USER lexa WITH PASSWORD '123qwe';
GRANT ALL PRIVILEGES ON DATABASE "regcity" to lexa;
psql -U alex cities - войти в бд

3. Пользователь для добавления/удаления/редактирования городов и регионов:
name='alex', email='alex@test.com', password='admin'

4. Создание таблиц в бд:
Входим в интерпритатор Pyhton
import models
from app import db
db.create_all()

5. Работа с приложением%
Приложение отображает Регионы и Города к ним (связь один ко многим).
Добавляем город, регион, отношение (прописывается в админке)
Редактировать, добавлять и удаления может только пользователь с правами admin (п.3).
Все остальные только чтение информации.



