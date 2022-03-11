from celery import shared_task

import random
import time


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_kwargs={"max_retries": 7, "countdown": 2},
)
def task_process_notification(self):
    if not random.choice([0, 1]):
        raise Exception()

    print("Executed")


@shared_task
def admin_task():
    print("Hello, this command is executed from an Admin panel")
