from django.urls import path
from apps.common.router import AppSimpleRouter

from .views import CreateUserAPIView

app_name = "access"

router = AppSimpleRouter()

urlpatterns = [
    path("create/user/", CreateUserAPIView.as_view()),
] + router.urls
