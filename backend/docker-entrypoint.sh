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

# Apply migrations for the 'manager' app
echo "Applying migrations for 'manager' app..."
python manage.py makemigrations manager
python manage.py migrate manager

# Preparing data
echo "Applying migrations for 'manager' app..."
python manage.py import_tickers_data
python manage.py import_data_from_coinbase
python manage.py import_data_from_balanz 1
python manage.py import_data_from_balanz 2

python manage.py collectstatic --no-input # this move all static files to server

gunicorn brucetrader.wsgi:application --bind 0.0.0.0:8081

echo "Django docker is fully configured successfully."

exec "$@"