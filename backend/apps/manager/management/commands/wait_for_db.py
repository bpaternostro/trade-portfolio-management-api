# your_app/management/commands/wait_for_db.py

import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = 'Wait for the database to be available'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Waiting for the database Bruce...'))
        max_retries = 30
        retry_count = 0
        while retry_count < max_retries:
            try:
                connections['default'].ensure_connection()
                print("Database connection established.")
                break
            except OperationalError:
                print("Database connection failed. Retrying...")
                retry_count += 1
                time.sleep(1)
        else:
            raise Exception("Unable to establish database connection.")

        self.stdout.write(self.style.SUCCESS('Database available!'))