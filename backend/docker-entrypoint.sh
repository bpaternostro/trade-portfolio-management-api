#!/bin/bash

# Wait for the database to be ready
echo "Waiting for database to be ready..."
python manage.py wait_for_db

# Apply core migrations
echo "Applying core migrations..."
python manage.py migrate admin
python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate sessions

# Apply migrations for the 'sections' app
echo "Applying migrations for 'sections' app..."
python manage.py makemigrations sections
python manage.py migrate sections

python manage.py collectstatic --no-input # this move all static files to server

gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

echo "Django docker is fully configured successfully."

exec "$@"