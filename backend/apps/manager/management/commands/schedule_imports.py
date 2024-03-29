# myapp/management/commands/my_scheduler.py
import schedule
import time
from django.core.management.base import BaseCommand
from django.core.management import execute_from_command_line

class Command(BaseCommand):
    help = 'Run scheduled tasks using the schedule library'
    
    def handle(self, *args, **options):
        # Define your task to be executed every N minutes
        TIME_INTERVAL = 35
        # Define your tasks
        def task_coinbase():
            self.stdout.write(self.style.SUCCESS('Running import data from coinbase'))
            try:
                execute_from_command_line(['manage.py', 'import_data_from_coinbase'])
            except Exception as e:
                self.stdout.write(self.style.WARNING('It was not possible to execute coinbase'))
        
        def task_balanz_1():
            self.stdout.write(self.style.SUCCESS('Running import cedears data from balanz'))
            try:
                execute_from_command_line(['manage.py', 'import_data_from_balanz', "1"])
            except Exception as e:
                self.stdout.write(self.style.WARNING('It was not possible to execute balanz 1'))
                
        def task_balanz_2():
            self.stdout.write(self.style.SUCCESS('Running import stock data from balanz'))
            try:
                execute_from_command_line(['manage.py', 'import_data_from_balanz', "2"])
            except Exception as e:
                self.stdout.write(self.style.WARNING('It was not possible to execute balanz 2'))
                
        # Schedule the task
        schedule.every(TIME_INTERVAL).minutes.do(task_coinbase)
        schedule.every(TIME_INTERVAL).minutes.do(task_balanz_1)
        schedule.every(TIME_INTERVAL).minutes.do(task_balanz_2)

        while True:
            schedule.run_pending()
            time.sleep(1)