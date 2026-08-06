from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView, CreateCircleView

from .views import RegisterView, CreateCircleView, JoinCircleView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),

    path("circles/", CreateCircleView.as_view()),
    path("circles/join/", JoinCircleView.as_view()),
]