[![Deploy Status](https://github.com/sadsadhead/kittygram_final/actions/workflows/main.yml/badge.svg)](https://github.com/sadsadhead/kittygram_final/actions/workflows/main.yml)

## KITTYGRAM

###   Описание проекта 

 Kittygram представляет собой сервис для обмена фотографиями кошек, ориентированный на любителей этого домашнего питомца. Сервис разработан с целью обеспечения возможности пользователям загружать изображения своих котов и просматривать фотографии, размещенные другими пользователями. В рамках проекта строго запрещается загружать изображения других видов домашних животных, таких как собаки или лошади.

 

###  Функциональность 

-   Публикация фотографий кошек. 

-  Просмотр фотографий, опубликованных другими пользователями. 

### Технологический стек 

####  Backend 

-  Django  

-  Django REST Framework 

-  Psycopg2-binary  

-  Pytest  

    

-  Gunicorn

    

#### Frontend 

-  React 

#### Сервер 

-  Nginx 

### Развёртывание проекта 

####  Клонировать репозиторий проекта с помощью команды: 

` git clone https://github.com/sadsadhead/kittygram_final.git `

#### Перейти в корневую директорию проекта: 

`cd kittygram_final `

#### Запустить Docker Compose для развёртывания контейнеров: 

`docker-compose up --build `

После успешного развёртывания проект будет доступен по адресу **http://localhost:80/.** 

### Как заполнить .env 

 Создать файл .env в корневой директории проекта и заполнить следующим образом: 

  

```
POSTGRES_DB=<база данных>
POSTGRES_USER=<имя пользователя>
POSTGRES_PASSWORD=<пароль>
DB_NAME=<имя базы данных>
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<секретный ключ Django>
ALLOWED_HOSTS=<разрешенные хосты>
DB_PLUG=<переключение БД на sqlite для тестирования - on/off>
DEBUG=<debug-режим Django - True/False>
```

### Автор 

 Автор проекта Kittygram - [sadsadhead](https://github.com/Sadsadhead).
