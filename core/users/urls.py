from django.urls import path

from core.users.views import UserListApi

urlpatterns = [path("", UserListApi.as_view(), name="list")]