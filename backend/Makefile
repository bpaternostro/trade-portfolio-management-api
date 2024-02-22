prepare:
	make migrations
	make migrate
#Si se rompe esto, sacar las foreing keys de la tabla customers a routines, hacer una primer pasada y despues habilitarlas

run:
	make migrate
	pipenv run python manage.py runserver

migrate:
	pipenv run python manage.py migrate
	pipenv run python manage.py migrate manager
	
migrations:
	pipenv run python manage.py makemigrations manager

run-site:
	docker compose up -d --remove-orphans

import_all:
	pipenv run python manage.py import_tickers_data

process_api_data:
	pipenv run python manage.py import_data_from_coinbase
	pipenv run python manage.py import_data_from_balanz 1
	pipenv run python manage.py import_data_from_balanz 2