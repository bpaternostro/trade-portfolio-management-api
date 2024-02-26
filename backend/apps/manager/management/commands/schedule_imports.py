# myapp/management/commands/my_scheduler.py
import schedule
import time
import threading
from django.core.management.base import BaseCommand
from django.core.management import execute_from_command_line

class Command(BaseCommand):
    help = 'Run scheduled tasks using the schedule library'
    
    def handle(self, *args, **options):
        # Define your task to be executed every N minutes
        TIME_INTERVAL = 5
        # Define your tasks
        def task_coinbase():
            self.stdout.write(self.style.SUCCESS('Running import data from coinbase'))
            execute_from_command_line(['manage.py', 'import_data_from_coinbase'])

        def task_balanz_1():
            self.stdout.write(self.style.SUCCESS('Running import cedears data from balanz'))
            execute_from_command_line(['manage.py', 'import_data_from_balanz', 1])

        def task_balanz_2():
            self.stdout.write(self.style.SUCCESS('Running import stock data from balanz'))
            execute_from_command_line(['manage.py', 'import_data_from_balanz', 2])

        # Schedule the task
        schedule.every(TIME_INTERVAL).minutes.do(task_coinbase)
        schedule.every(TIME_INTERVAL).minutes.do(task_balanz_1)
        schedule.every(TIME_INTERVAL).minutes.do(task_balanz_2)

        # Create a thread to run the scheduler
        def run_scheduler():
            while True:
                schedule.run_pending()
                time.sleep(1)

        # Start the scheduler thread
        scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        scheduler_thread.start()

        # Keep the main thread alive (Django management command does not exit)
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            pass
