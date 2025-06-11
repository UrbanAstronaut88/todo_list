from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("task/create/", views.task_create, name="task-create"),
    path("task/<int:pk>/update/", views.task_update, name="task-update"),
    path("task/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("task/<int:pk>/complete/", views.toggle_complete, name="toggle-complete"),

# tags
    path("tags/", views.tag_list, name="tag-list"),
    path("tags/create/", views.tag_create, name="tag-create"),
    path("tags/<int:pk>/update/", views.tag_update, name="tag-update"),
    path("tags/<int:pk>/delete/", views.tag_delete, name="tag-delete"),
]
