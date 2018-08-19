# smartDiag

Deployed on AWS Cloud:

http://smartdiagapp.a6ygmbqea4.ap-south-1.elasticbeanstalk.com/



Better prediction to help doctors by using Deep Learning in various fields of Medical Science.



Front-end:
Bootstrap 4,
Materialize,
VanillaTilt JS,
jQuery

Back-end:
Django

Database:
SQLite3




SETUP The Project ->

virtualenv djangoenv

cd djangoenv

cd Scripts

activate

pip install -r requirements.txt




Add 'livereload' to the INSTALLED_APPS, before 'django.contrib.staticfiles' if this is used:

INSTALLED_APPS = (
    ...
    'livereload',
    ...
)

Add 'livereload.middleware.LiveReloadScript' to MIDDLEWARE_CLASSES (probably at the end):

MIDDLEWARE_CLASSES = (
    ...
    'livereload.middleware.LiveReloadScript',
)

> python manage.py livereload  -> hot reloading

> python manage.py runserver  -> to start the server
