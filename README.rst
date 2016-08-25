My_Geonode
========================

You should write some docs, it's good for the soul.

Installation
------------

Install the native dependencies for your platform.

Install virtualenv and virtualenvwrapper, Create a local virtual environment for your project and install Django into it.::

    $ mkdir ~/VirtualEnvs
    $ cd ~/VirtualEnvs
    $ virtualenv my_geonode
    $ pip install Django==1.8.12

Create a new template based on the geonode example project.::

    $ django-admin.py startproject my_geonode --template=https://github.com/GeoNode/geonode-project/archive/master.zip -epy,rst,yml -n Vagrantfile

.. note:: You should NOT use the name geonode for your project as it will conflict with the default geonode package name.
.. note:: Put your "my_geonode" project under version control using GitHub or similar.

Using ansible for Automated Deploys
-----------------------------------

In order to install for production on a remote machine or to a local VM for development, you will need to install ansible::

     $ sudo pip install ansible

Note: It is advisable to install ansible system wide using sudo

Next, you will need to install the ansible role for geonode::

     $ ansible-galaxy install ortelius.geonode

Setting up a vagrant box
-------------------------

Setup VirtualBox and install vagrant.
Edit the playbook.yml file:

    + Set remote_user and deploy_user to "vagrant".
    + Set github_user to the username of your GitHub account.
    + Set server_name to 192.168.56.151 (This is the same IP address as used in the Vagrantfile.).

Edit Vagrantfile and add the line as follows:

    config.vm.network :private_network, ip: "192.168.56.151"

Remove this line from Vagrantfile:

    config.vm.network "forwarded_port", guest: 80, host: 8000

Then setup your virtual machine with:

    $ vagrant up

Note: the vagrant installation uses Ansible, so you will need to follow the steps in the previous section.

Usage in production
-------------------

Update /etc/ansible/hosts to include your webservers host or dns entry::

    [webservers]
    ###.###.###.###

Then you can run the playbook to install the my_geonode  project::

    $ ansible-playbook playbook.yml

Basic Usage
-----------

Log on to the Virtual Machine vis SSH and setup the database (creating the database is a one-time setup):

    $ vagrant ssh
    $ cd my_geonode
    $ python manage.py syncdb

.. note:: You will be asked to provide credentials for the superuser account.

Start the development server::

    $ python manage.py runserver
