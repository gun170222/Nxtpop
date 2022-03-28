mysql -u root -p
create database nxtpopdb;
pip install django
pip install mysqlclient
python manage.py migrate
pip install django-widget-tweaks
python manage.py makemigrations submitapp
python manage.py migrate
python manage.py runserver
http://localhost:8000