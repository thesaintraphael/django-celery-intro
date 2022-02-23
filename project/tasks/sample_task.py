from django.contrib.auth import get_user_model as User

from celery import shared_task

import random
import string
import time

from .decorators.celery_transaction import CeleryTransaction


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
@CeleryTransaction(max_retries=5)
def task_transaction_test():
    username = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    User.objects.create(username=username, password="sdcnkKJDsn2738$%")
