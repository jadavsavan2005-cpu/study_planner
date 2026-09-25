from django.contrib import admin
from django.urls import path

from studyplanner import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.task_list, name="task_list"),
    path("task/add/", views.add_task, name="add_task"),
    path("task/<int:task_id>/edit/", views.edit_task, name="edit_task"),
    path("task/<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("task/<int:task_id>/toggle/", views.toggle_task, name="toggle_task"),

    path("subjects/", views.subject_list, name="subject_list"),
    path("subjects/add/", views.add_subject, name="add_subject"),
    path("subjects/<int:subject_id>/delete/", views.delete_subject, name="delete_subject"),
]
