# API для Yatube

## Описание
Yatube - это блог для публикации постов и комментариев для обсуждение фильмов. Проект состоит из бекенда на Django.

API для проекта Yatube - это решение готовое к взаимодействию с фронтендом блога Yatube, где у пользователей есть следующие возможности:
- регистрация
- публикация постов
- публикация комментариев
- подписка на публикации прочих пользователей сервиса

В данном проекте моей главной задачей было написать API бекенда сервиса для осуществления взаимодействия с фронтендом на React. Бекенд был мною разработан на Django REST Framework. Тестирование API в ходе разработки я проводил в Postman.

## Стек технологий проекта
![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/-Django-black?style=for-the-badge&logo=Django)
![DRF](https://img.shields.io/badge/-Django_REST_Framework-black?style=for-the-badge&logo=DRF)
![SQLite](https://img.shields.io/badge/-SQLite-black?style=for-the-badge&logo=SQLite)
![Postman](https://img.shields.io/badge/-Postman-black?style=for-the-badge&logo=postman)
![Redoc](https://img.shields.io/badge/-Redoc-black?style=for-the-badge&logo=redoc)

### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Invoker9999/api_final_yatube.git
```

```
cd api_final_yatube/
```
Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
- в командной строке bash:
```
source venv/Script/activate
```
- в командной строке powershell:
```
. venv/Script/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
При необходимости обновить pip:
```
python -m pip install --upgrade pip
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
Документация к API проекта Yatube находится на эндпоинте ReDoc:
```
http://127.0.0.1:8000/redoc/
```
