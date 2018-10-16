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

Install Python3, pip in your system.

> virtualenv djangoenv

Move to your virtual environment - 
> cd djangoenv

> cd Scripts

Activate Your virtual environment.
> activate

Install all the reruired packages using the following command - 
> pip install -r requirements.txt

> python manage.py runserver  -> to start the server


Add 'livereload' to the INSTALLED_APPS, before 'django.contrib.staticfiles' if this is used:

INSTALLED_APPS = (
    ...
    'livereload',
    ...
)


Do the following if you're gonna work further on the front-end.

Add 'livereload.middleware.LiveReloadScript' to MIDDLEWARE_CLASSES (probably at the end):

MIDDLEWARE_CLASSES = (
    ...
    'livereload.middleware.LiveReloadScript',
)

> python manage.py livereload  -> hot reloading
