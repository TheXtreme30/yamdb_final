# YaMDb
![example workflow](https://github.com/TheXtreme30/yamdb_final/blob/master/.github/workflows/main.yml/badge.svg)

Проект YaMDb собирает отзывы пользователей на произведения.

### Технологии
- python 3.8.5
- django 3.0.5

### Запуск проекта
- В папке с файлом manage.py выполните команду:
```
docker-compose up
``` 
- Выполните миграции
```
docker-compose exec web python manage.py migrate --noinput
``` 
- Команда для создания суперпользователя
```
docker-compose exec web python manage.py createsuperuser
``` 

### Автор
Сергей. Студент Яндекс.Практикум 

