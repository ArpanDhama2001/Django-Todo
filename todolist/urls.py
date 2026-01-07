from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("delete_task/<task_id>", views.delete_task, name="delete_task"),
    path("mark_incomplete/<task_id>", views.mark_incomplete, name="mark_incomplete"),
    path("mark_complete/<task_id>", views.mark_complete, name="mark_complete"),
    path("edit_task/<task_id>", views.edit_task, name="edit_task"),
    path("profile", views.profilepage, name="profilepage"),
    path("<int:todo_id>/", views.todo_details_page, name="todo_details")
]