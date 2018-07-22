# smartDiag
Better prediction to help doctors by using Machine Learning in various fields of Medical Science.

Front-end libraries used:
Bootstrap 4
Materialize
Vanilla JS
jQuery

Back-end:
Django

Database:
SQLite3




SETUP The Project ->

Install package:

> pip install django-livereload-server

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

Upload file feature added.
