# Сервис справочников ОТ

Сервис предоставляет доступ к следующим справочникам:
 - ЕРВК
 - Кодексы РФ
 - Преобразования текстовое значение:числовое значение
 - ОКВЭД



# Сборка 

Осуществляется с помощью инструкции описанной в файле /docker/docker-compose.yml

### Сервисы: 
- База данных postgresq из образа library/postgres:14.1 (https://hub.docker.com/_/postgres)
  
- Веб-сервис Nginx/Unit + FastAPI из образа debian/bullseye-slim (https://hub.docker.com/_/debian)
  
## Настройки переменных окружения

### Наименование проекта для docker-compose

__COMPOSE_PROJECT_NAME=catalogues__

### Настройки контейнера Postgres

__POSTGRES_USER=postgres__

__POSTGRES_PASSWORD=password__

__POSTGRES_PORT=5432__

__POSTGRES_EXTERNAL_PORT=17001__

__PGDATA=/var/lib/postgresql/data/pgdata__
### Настройки контейнера FastAPI 

__DB_USER=fastapi__

__DB_PASSWORD=fastapi_password__

Файл .env необходимо поместить в директорию сборки /docker/.env

### Контейнер БД 

https://hub.docker.com/_/postgres

Сценарий для сборки контейнера БД описан в /docker/database/Dockerfile, включая небходимые скрипты инициализации в /docker/database/init, где:
1.  *.sh это скрипт для создания схем и пользователей, 
2.  *.sql набор данных для создания таблиц и записи данных

### Контейнер веб-сервиса

Cценарий для сборки контейнера сервиса описан в /docker/app/Dockerfile, где 
1. requirements.txt это зависимости для Python3
   https://pip.pypa.io/en/stable/cli/pip_install/#requirements-file-format
2. config.json конфигурация приложения для nginx/unit
    https://unit.nginx.org/configuration/#python

### Развертывание

Сценарий развертывания контейнеров в рамках проекта описан в docker-compose.yml

1. Контейнер БД подключается к двум сетям:
   - общая для всех контейнеров БД для упрощения возможности подключения через клиентские приложения (PGAdmin, CloudBeaver  и т.д.)
   https://docs.docker.com/network/bridge/
   - общая сеть для контейнеров веб-сервиса и БД
   IP настраивается автоматически.
   IP хоста-контейнера с БД передается через docker 
   https://docs.docker.com/config/containers/container-networking/
2. Для контейнера с веб-сервисом описана инструкция и зависимость от контейнера с БД. Контейнер с веб-сервисом стартует только после полной готовности контейнера БД (healthcheck/health)
3. Настройки использования ресурсов описаны в docker-compose.yml
   https://docs.docker.com/compose/compose-file/compose-file-v3/
   https://docs.docker.com/compose/production/

### Рекомендации

Рекомендуется настроить использовать прокси-сервер для доступа к веб-сервису