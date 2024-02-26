import schedule
import time

from .apps.manager.management.commands import import_data_from_coinbase, import_data_from_balanz

# Define your tasks
def task_coinbase():
    import_data_from_coinbase()

def task_balanz_1():
    import_data_from_balanz(1)

def task_balanz_2():
    import_data_from_balanz(2)

# Schedule tasks to run every 45 minutes
schedule.every(5).minutes.do(task_coinbase)
schedule.every(5).minutes.do(task_balanz_1)
schedule.every(5).minutes.do(task_balanz_2)

# Keep the script running to execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)