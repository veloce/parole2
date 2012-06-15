Guide de démarrage
=================

## Prérequis

* Python 2.7
* Virtualenv (voir ce [guide](http://docs.python-guide.org/en/latest/starting/install/linux/) pour l'installation)

## Étapes

### Cloner le repository git

    $ git clone git@bitbucket.org:veloce/parole2-django.git parole2
    $ cd parole2

### Créer et activer le virtualenv

    $ virtualenv venv --distribute
    $ . venv/bin/activate

### Installer les dépendances

    $ pip install -r requirements.txt

### Configurer la base de donnée

    $ cp local_settings.py.txt local_settings.py # pour utiliser sqlite
    $ python manage.py syncdb

### Lancer le serveur web

    $ python manage.py runserver
        
## Deployer sur heroku

### Installer la [heroku toolbelt](https://toolbelt.herokuapp.com/osx)

    $ heroku login
    $ git remote add heroku git@heroku.com:stormy-sunset-3188.git
    $ git push heroku master
