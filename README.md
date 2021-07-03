# Setup

## Install dependencies
`pip install selenium`
Download *https://github.com/mozilla/geckodriver/releases* and place it under /usr/bin
`pip install django`

## Setup django project
`$ django-admin startproject superlists .`
`$ python manage.py runserver`

# Developing web applications
## Setting up the Django project
*Create an app*
`$ python manage.py startapp lists`

Running the Django dev server
`$ python manage.py runserver`

Running the functional tests
`$ python functional_tests.py`

Running the unit tests
`$ python manage.py test`

The unit-test/code cycle
* Run the unit tests in the terminal.
* Make a minimal code change in the editor.
* Repeat!

## Setting up the Django object database
Migrate current model to the "database"
`$ python manage.py makemigrations`

Create the actual configured DATABASE
`$ python manage.py migrate`

Recreate the Database
`$ rm db.sqlite3`
`$ python manage.py migrate --noinput`