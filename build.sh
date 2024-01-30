#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install -r requirements.txt

python ./www/manage.py collectstatic --no-input
python manage.py migrate