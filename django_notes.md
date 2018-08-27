Command for making a virtualenv

Remember! I only use the number 3 after python to make it run as python3 enviroment.

**python3 -m venv ll_env**

venv is a python module, which we use to create a new virtual enviroment called
ll_env.

To activate the new virtual enviroment. Run this command:

source ll_env/bin/activate

This will start the virtual enviroment.

To deactivate, write 'deactivate'

When you have activated the virtual env, write this command to install django:

'''bash
pip3 install Django
'''
This will make us run django only under this virtual enviroment.

To create a django project, so will we write this:

'''bash
django-admin.py startproject learning_log .
'''

Remember, the . after log is for marking CURRENT directory.

To make a database for our project:

'''bash
python3 manage.py migrate
'''

To start an app, we can write this:

'''bash
python3 manage.py startapp learning_logs
'''

While in the virtual env.

If we have made some changes to the models, we run:

'''bash
python3 manage.py makemigrations learning_logs
'''

and then migrate/update(?)

'''bash
python3 manage.py migrate
'''

We can then view the project by running this terminal command:

'''python 
python3 manage.py runserver
'''
