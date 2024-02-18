from django.urls import include, path
from .views import MessageView, UserView


urlpatterns = [
    path("todo", MessageView.as_view(), name="todo-api"),
    path("todo/<str:pk>", MessageView.as_view(), name="todo-detail-api"),
    path("user/<int:pk>", UserView.as_view(), name="todo-detail-api")

]
