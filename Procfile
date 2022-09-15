web: gunicorn website.wsgi:application --log-file -
python manage.py collectstatic --noinput
manage.py migrate