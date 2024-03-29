from django.urls import include, path
from .views import MessageView, UserView, CategoryView, add_category


urlpatterns = [
    path("message", MessageView.as_view(), name="todo-api"),
    path("message/category", CategoryView.as_view(), name="todo-category-api"),
    path("message/<str:pk>", MessageView.as_view(), name="todo-detail-api"),
    path("user/<int:pk>", UserView.as_view(), name="todo-user-api"),
    path("message/<str:message_id>/category/<str:category_id>",
         add_category, name="todo-message-category-api")

]
