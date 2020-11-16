#!/bin/bash

if [ "$1" = 'runserver' ]; then
    exec pipenv run ./manage.py runserver
fi

if [ "$1" = 'bash' ]; then
    pipenv shell
fi

exec "$@"
