python manage.py migrate
python manage.py livereload --host "0.0.0.0" &
exec python manage.py runserver 0.0.0.0:8000
