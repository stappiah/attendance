from django.urls import path
from . import views

urlpatterns = [
    path("course", views.CreateCourseView.as_view()),
    path("list_course", views.RetrieveCourse.as_view()),
    path("delete_course/<int:pk>", views.DeleteCourseView.as_view()),
]
