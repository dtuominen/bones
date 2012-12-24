# Djangobones
-----

<table>
<tr>
<th>Maintainer:</th>
<td>Dylan Tuominen:</td>
</tr>
</table>
-----

## Basic installation and use

* clone the repo
* create a virtualenvironment
* install the requirements
* create the initial database tables
* apply migrations
* create migrations for new apps
* create migrations for updated models
* apply migrations


        $ git clone git@github.com:dtuominen/bones.git
        $ mkvirtualenv --no-site-packages myproject
        $ pip install -r requirements.txt
        $ python manage.py syncdb
        $ python manage.py schemamigration --initial mybrandnewapp
        $ python manage.py schemamigration --auto basicapp
        $ python manage.py migrate


### General

Most of the basic boilerplate configuration is set

### Settings

Settings is now a module and related settings should thus be split
into their own files where it makes sense

### App structure

apps should be kept inside of the new apps/ folder located one level below manage.py

### Basic deployment

Basic fabric deployment/remote management scripts have been 
included in fabfile.py

### Included packages

* South
* django-extensions
* django-toolbar
* fabric

### Full dependency list

    Django==1.4.3
    Fabric==1.5.1
    South==0.7.6
    argparse==1.2.1
    distribute==0.6.28
    django-debug-toolbar==0.9.4
    django-extensions==1.0.2
    paramiko==1.9.0
    pycrypto==2.6
    wsgiref==0.1.2
