web: gunicorn --chdir djangodelights djangodelights.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py migrate