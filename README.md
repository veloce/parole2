Guide de démarrage
=================

## Prérequis

* Python 2.7
* Virtualenv (voir ce [guide](http://docs.python-guide.org/en/latest/starting/install/linux/) pour l'installation)

## Étapes

1. Cloner le repository git

    $ git clone git@bitbucket.org:veloce/parole2-django.git parole2
    $ cd parole2

2. Créer et activer le virtualenv

    $ virtualenv venv --distribute
    $ . venv/bin/activate

3. Installer les dépendances

    $ pip install -r requirements.txt

4. Configurer la base de donnée

    $ cp local_settings.py.txt local_settings.py # pour utiliser sqlite
    $ python manage.py syncdb

5. Lancer le serveur web

    $ python manage.py runserver
        
