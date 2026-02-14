## Environment

| env                         | возможные значения                     | описание                     |
|:----------------------------|:---------------------------------------|:-----------------------------|
| DJANGO_DEBUG                | true/false                             |                              |
| DJANGO_CSRF_TRUSTED_ORIGINS | http://example.com,https://example.com |                              |
| DJANGO_WEBSITE_DNS_NAME     | example.com                            |                              |
| DJANGO_EMAIL_HOST           |                                        |                              |
| DJANGO_EMAIL_PORT           |                                        |                              |
| DJANGO_EMAIL_USE_TLS        |                                        |                              |
| DJANGO_EMAIL_HOST_USER      |                                        |                              |
| DJANGO_EMAIL_HOST_PASSWORD  |                                        |                              |
| PGSERVICEFILE               |                                        |                              |
| PGPASSFILE                  |                                        |                              |

## Подключение к БД postgresql
| ОС      | Расположение файла                    |
|:--------|:--------------------------------------|
| windows | %APPDATA%\postgresql\.pg_service.conf |
| linux   | ~/.pg_service.conf                    |
```
[mood2anime]
host=hostname
user=username
dbname=database
port=port
sslmode=verify-full
sslrootcert=/path/to/server-ca.crt
sslcert=/path/to/client.crt
sslkey=/path/to/client.key
```

| ОС      | Расположение файла               |
|:--------|:---------------------------------|
| windows | %APPDATA%\postgresql\pgpass.conf |
| linux   | ~/.pgpass                        |
```
hostname:port:database:username:password
```

## Импортирование данных в БД
```python3 .\manage.py import --path ..\mood2anime_DB\data```