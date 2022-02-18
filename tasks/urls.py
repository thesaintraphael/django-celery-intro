from django.urls import path

from . import views

urlpatterns = [
    path("tasks/<task_id>/", views.get_status, name="get_status"),
    path("tasks/", views.run_task, name="run_task"),
    path("", views.home, name="home"),
]
