Starting guide
=================

## Prerequisites

* Python 2.7
* Virtualenv (see [this guide](http://docs.python-guide.org/en/latest/starting/install/linux/))

## Steps

### Clone repo

    $ git clone git@bitbucket.org:veloce/parole2-django.git parole2
    $ cd parole2

### Create and activate virtualenv

    $ virtualenv venv --distribute
    $ . venv/bin/activate

### Install dependencies

    $ pip install -r requirements.txt

### Configure database

    $ cp local_settings.py.txt local_settings.py # will use sqlite
    $ python manage.py syncdb

### Run web server

    $ python manage.py runserver

## Deploy on heroku

### Install the [heroku toolbelt](https://toolbelt.herokuapp.com/osx)

    $ heroku login
    $ git remote add heroku git@heroku.com:your-domain-name.git
    $ git push heroku master
