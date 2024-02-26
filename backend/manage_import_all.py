import schedule
import time
import os
from django.core.management import execute_from_command_line

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brucetrader.settings')
TIME_INTERVAL = os.environ.get('TIME_INTERVAL_API_PROCESS')

# Define your tasks
def task_coinbase():
    execute_from_command_line(['manage.py', 'import_data_from_coinbase'])

def task_balanz_1():
    execute_from_command_line(['manage.py', 'import_data_from_balanz', 1])

def task_balanz_2():
    execute_from_command_line(['manage.py', 'import_data_from_balanz', 2])

# Schedule tasks to run every 45 minutes
schedule.every(TIME_INTERVAL).minutes.do(task_coinbase)
schedule.every(TIME_INTERVAL).minutes.do(task_balanz_1)
schedule.every(TIME_INTERVAL).minutes.do(task_balanz_2)

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)