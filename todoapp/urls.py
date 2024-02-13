from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.todo, name="home"),
    path("create/", views.add_todo, name="add-todo"),
    path("<str:pk>", views.todo, name="todo"),
    path("update/<str:pk>/", views.update_todo, name="update-todo"),
    path("delete/<str:pk>/", views.delete_todo, name="delete-todo"),
]
