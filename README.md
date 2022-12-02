# Сервис по управлению космическими станциями.

### Описание

В сервисе хранится информация станциях и их позиции в пространстве. Через сервис можно создавать станции и изменять их позицию.

У станции 3 координаты: x, y, z. При запуске станции ее координаты по умолчанию равны: 100, 100, 100.
Станция исправно может двигаться только в диапазоне положительных координат. Если Станция вышла за эти координаты, мы считаем ее неисправной, даже если в будущем она вернулась обратно в разрешенную зону.

Позиция станции меняется через Указание: ось и значение смещения. За одно Указание можно сместиться только в одну сторону на неограниченное расстояние.
 
Станцию можно удалить или отправить на -999 координаты.

### Стек

- Python
- Django
- DRF 
- coverage 
- OpenAPI 
- Docker 
- Docker-compose
- PostgreSQL

### Запуск проекта

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:KseniyaGurevich/Space_station.git
```
- Cоздать и активировать виртуальное окружение.

- Установить зависимости:
```
poetry install
```
<hr>

<b>1) БЕЗ docker-compose с использованием базы данных sqlLite.</b>

- В файле < Space_station/station/station/.env > ввести:

```
RUNNING_IN_DOCKER = Yes
```
- Сделать миграции:
```commandline
python manage.py makemigrations
python manage.py migrate
```
- Можно загрузить базу данных:
```commandline
python manage.py loaddata data.json
```
- Запустить приложение:
```commandline
python manage.py runserver
```
- Чтобы запустить приложение в docker-контейнере:
```commandline
docker build -t "name_image" .
docker run --name "name_container" -it -p 8000:8000 "name_image"
```
<hr>

<b>2) ЧЕРЕЗ docker-compose с использованием базы данных PostgreSQL</b>
- В файле < Space_station/station/station/.env > ввести:</p>

```
RUNNING_IN_DOCKER = No
```

- В файле < Space_station/.env > записать переменные окружения:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME="name data base in postgres"
POSTGRES_USER="name user"
POSTGRES_PASSWORD="password user"
DB_HOST=db
DB_PORT=5432
```

- В папе infra запустить docker-compose:
```
docker-compose up
```
- Проверить, нет ли в контейнере web базы данных sqlite. Если есть, то удалить её:
```commandline
docker-compose exec -it web bash
  ls
  rm db.sqlite3
  exit
```

- Запустить миграции в контейнере web:
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

- Сделать локально копию базы данных:
```
docker-compose exec web python -Xutf8 ./manage.py dumpdata > data.json
```

- Сохранить копию базы данных в контенер web:
```
docker-compose cp data.json web:app/
```
- Загрузить базу данных из data.json:
```
docker-compose exec web python manage.py loaddata data.json
```

<hr>

### Доступные адреса 

http://127.0.0.1:8000/admin/ - админка

http://127.0.0.1:8000/swagger-ui/ - документация

http://127.0.0.1:8000/stations/

http://127.0.0.1:8000/stations/<station_id>/

http://127.0.0.1:8000/stations/<station_id>/state/

http://127.0.0.1:8000/auth/users/ - авторизация

<hr>

### Тесты:

Space_station / station / api/ tests.py

### Отчёт о покрытии тестами в можно посмотреть в директории:

Space_station / station / htmlcov / index.html

<hr>

Затраченное время ~ 20 часов