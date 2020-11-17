#!/bin/bash

if [ ! -f .env ]; then
    PW=`base64 /dev/urandom | head -c 50`
    echo "SECRET_KEY=$PW" > .env
fi

if [ "$1" = 'runserver' ]; then
    pipenv run ./manage.py migrate
    exec pipenv run ./manage.py runserver 0:8000
fi

if [ "$1" = 'test' ]; then
    exec pipenv run ./manage.py test
fi

if [ "$1" = 'bash' ]; then
    pipenv shell
fi

exec "$@"
