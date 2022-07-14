# SimpleChatApp
A simple web chat app that enables users send messages and communicate with each other.

---
## Prerequisites
The software versions used in this project are:

1. Python3.8.2
2. Pip
3. Django 2.2.15 (LTS)
4. Virtualenv
5. Redis
6. Django channels 2
7. Postgres

---
## Installation
1. To begin with installation, navigate to the desired directory where you want to start the project and clone this repository.
2. Create a virtual environment to install all the necessary pacakges. You can follow the following tutorial, 
[Virtual Environment](https://docs.python.org/3/library/venv.html)
3. Navigate to the '/ChatApp' directory and install the required packages by typing;
    > pip3 install -r requirements.txt
4. Before making all changes to the database, open the 'settings.py' file and make changes to the database to configure the correct Database as shown below:
```
DB_NAME = 'chatapp'
DB_USER = 'franchise'
DB_PASSWORD = '#####'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. Afterwards, make migrations to the database by typing on the terminal;
    > python3 manage.py migrate
6. Update settings with **CHANNEL_LAYERS** configuration
```
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```
7. To start the local server, type the following;
    > python3 manage.py runserver
8. Create the superuser using the following code then enter your email and password.
    > python3 manage.py createsuperuser

