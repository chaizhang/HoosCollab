#!/usr/bin/env bash

# install dependencies
pip install -r requirements.txt

# collect static files into /staticfiles
python manage.py collectstatic --noinput --clear

# apply migrations to Supabase database
python manage.py migrate