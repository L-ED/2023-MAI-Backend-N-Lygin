#!/bin/sh

sleep 5


service nginx start
python3 manage.py migrate
gunicorn project.wsgi 127.0.0.1:8000

exec "$@"