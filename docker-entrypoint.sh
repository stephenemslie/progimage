#!/bin/bash

if [ "$1" = 'runserver' ]; then
    pipenv run ./manage.py migrate
    exec pipenv run ./manage.py runserver 0:8000
fi

if [ "$1" = 'test' ]; then
    exec pipenv run ./manage.py test

if [ "$1" = 'bash' ]; then
    pipenv shell
fi

exec "$@"
