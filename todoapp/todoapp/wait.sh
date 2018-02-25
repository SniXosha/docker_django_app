#!/bin/bash


sleep 5;
python3 manage.py makemigrations;
python3 manage.py migrate;
python3 -c "import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'todoapp.settings'
import django
django.setup()
from django.contrib.auth.management.commands.createsuperuser import get_user_model
if get_user_model().objects.filter(username='$DJANGO_SU_NAME'): 
    print('Super user already exists. SKIPPING...')
else:
    print('Creating super user...')
    print('Username is: {}'.format('$DJANGO_SU_NAME'))
    u = get_user_model()._default_manager.db_manager('$DJANGO_DB_NAME').create_superuser(username='$DJANGO_SU_NAME', email='$DJANGO_SU_EMAIL', password='$DJANGO_SU_PASSWORD')
    u.save()
    print('Super user created...')"
python3 manage.py runserver 0.0.0.0:8000;
