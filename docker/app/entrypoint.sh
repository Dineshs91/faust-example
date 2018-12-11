#! /bin/bash

set -e

python manage.py migrate

gunicorn faust_proj.wsgi -k eventlet -w 1 -b 0.0.0.0:8020 --reload
