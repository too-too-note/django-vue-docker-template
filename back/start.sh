#!/bin/bash
sleep 5
# python manage.py makemigrations
# python manage.py migrate
# python manage.py collectstatic --noinput
uwsgi --socket :8001 --module mainproject.wsgi