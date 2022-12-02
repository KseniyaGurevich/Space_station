#Сервис по управлению космическими станциями.

<hr>
<p> Чтобы запустить приложение БЕЗ docker-compose (локально или в docker-контейнере) с использованием базы данных sqlLite, нужно:<p/>
<p>В файле .env ввести:</p>

```
RUNNING_IN_DOCKER = Yes
```

Путь к файлу .env (лежит в папке с settings.py):

```
Space_station/station/station/.env
```


<hr>

Чтобы запустить приложение ЧЕРЕЗ docker-compose с использованием базы данных PostgreSQL
###Запустить Docker c бд sqlite
python manage.py migrate
docker build -t station2 .
docker run --name Station2 -it -p 8000:8000 station2


Загрузка базы данных:
python -Xutf8 ./manage.py dumpdata > data.json



Space_station/.env:

DB_ENGINE=django.db.backends.postgresql
DB_NAME="name data base in postgres"
POSTGRES_USER=name user
POSTGRES_PASSWORD=password user
DB_HOST=db
DB_PORT=5432



###после запуска docker-compose запустить миграции в контейнере web:
docker-compose exec web python manage.py migrate


###Сделать локально копию базы данных:
docker-compose exec web python -Xutf8 ./manage.py dumpdata > data.json

###Загрузить базу данных в контенер web
docker-compose cp data.json web:app/

###загрузить базу данных из data.json
docker-compose exec web python manage.py loaddata data.json


### Зайти в контейр web можно командой:
docker-compose exec -it web bash

###сделать миграции
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

###загрузить базу данных из data.json
docker-compose exec web python -Xutf8 ./manage.py dumpdata > data.json
docker-compose cp data.json web:app/
docker-compose exec web python manage.py loaddata data.json

http://127.0.0.1:8000/admin/ - админка
http://127.0.0.1:8000/swagger-ui/ - документация



Затраченное время:  20 часов