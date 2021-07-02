# Setup

## Install dependencies
`pip install selenium`
Download *https://github.com/mozilla/geckodriver/releases* and place it under /usr/bin
`pip install django`

## Setup django project
`$ django-admin startproject superlists .`
`$ python manage.py runserver`

## Using the Django project
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

