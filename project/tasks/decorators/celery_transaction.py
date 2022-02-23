import functools

from django.db import transaction

from celery import shared_task


class CeleryTransaction:
    """
    This is a decorator we can use to add custom logic to our Celery task
    such as retry or database transaction
    """

    def __init__(self, *args, **kwargs):
        self.task_args = args
        self.task_kwargs = kwargs

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            try:
                with transaction.atomic():
                    return func(*args, **kwargs)
            except Exception as e:
                # task_func.request.retries
                raise task_func.retry(exc=e, countdown=5) from e

        task_func = shared_task(*self.task_args, **self.task_kwargs)(wrapper_func)
        return task_func
