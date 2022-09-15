web: gunicorn --pythonpath djangodelights djangodelights.wsgi
release: python djangodelights/manage.py migrate
heroku ps:scale web=1

