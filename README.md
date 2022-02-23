### Introduction Celery + Django combination to run Shcheduled Tasks

## Run locally

Clone repository

```bash
git clone https://github.com/thesaintraphael/django-celery-intro.git
```

## Build docker container

```bash
docker-compose up -d --build
```

## Run tests

```bash
docker-compose exec web python -m pytest
```


## Used Resources
```bash
1. https://testdriven.io/blog/django-and-celery/
2. https://realpython.com/asynchronous-tasks-with-django-and-celery/
3. https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
```
