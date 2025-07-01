from django.urls import path
from users.views import UserCreateAPIView
from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="user-create"),
]
