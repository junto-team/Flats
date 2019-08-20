### Назначение
Проект предназначен для формирования фидов с объектами недвижимости Mezon. 
Фиды используют либо формат Яндекс.Недвижимость, либо ЦИАН.

### Технологический стэк   
- Django 1.11
- Gunicorn
- Ngnix

### Алгоритм
1. Раз в день запускается задача по обновлению фида.
2. Загружаются все объекты из БД мезона.
3. Формируются по-отдельности новые фиды.
4. Фиды сохраняются в БД и становяться доступны по своим URL.
5. Каждый сервис скачивает каждый свой фид по настроенному заранее URL.

### Установка
1. Скачиваем проект.
2. Создаем фаил окружения `.env` и заполняем его.
3. Создаем виртуальное окружение питона и устанавливает туда пакеты из requirements.txt .
4. Устанавливаем Gunicorn и Nginx. https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
5. Добавляем в крон команду на обновление фидов раз в сутки.

#### Параметры окружения:
```
# Cекретный ключ Django
SECRET_KEY=34hj43j5h8ue8rij43r43f

# Параметры доступа к базе данных Mezon в формате dj-database-url
MEZON_DATABASE_URL=DATABASE_TYPE://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME

# Режим дебага
DEBUG=False
```

#### Пример конфигурации Gunicorn:   
```
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/mezon
ExecStart=/home/ubuntu/venv-mezon/bin/gunicorn --access-logfile - --workers 2 --bind unix:/home/ubuntu/mezon/flats.sock flats.wsgi:application

[Install]
WantedBy=multi-user.target
```

#### Пример конфигурации Nginx:
```
server {
    listen 80;
    server_name <место для IP сервера>;

    keepalive_timeout  1000;
    client_body_timeout 1000;
    fastcgi_read_timeout 1000;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/mezon/flats.sock;
    }
}
```

#### Пример команд для обновления фидов:
```
#!/bin/bash
cd /home/ubuntu/mezon/
source /home/ubuntu/venv-mezon/bin/activate
python manage.py createcachetable
python manage.py generate_yrl
deactivate
```

#### Пример насткройки CRON:
```
0 2 * * * cd /home/ubuntu/ && ./update_feed.sh
```

#### Структура директорий для которых привидены примеры:
```
/home/ubuntu/
├── mezon
│   ├── base
│   ├── db.sqlite3 - cоздает Django
│   ├── flats
│   ├── flats.sock - создает Gunicorn
│   ├── manage.py
│   └── requirements.txt
├── update_feed.sh - команды для обновления фида
└── venv-mezon - виртуальное окружение virtualenv
    ├── bin
    ├── include
    └── lib
```