from django.urls import include, path
from .views import MessageView


urlpatterns = [
    path("todo", MessageView.as_view(), name="todo-api"),
    path("todo/<str:pk>", MessageView.as_view(), name="todo-detail-api")
]
