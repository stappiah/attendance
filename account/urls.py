from django.urls import path
from . import views

urlpatterns = [
    path("register", views.UserRegistrationView.as_view()),
    path("login", views.CustomAuthModel.as_view()),
]
