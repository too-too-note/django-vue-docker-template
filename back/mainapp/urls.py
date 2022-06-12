from django.urls import path

from .views import *

urlpatterns = [
    path("test/", TaskView.as_view(), name="task_list"),
]
