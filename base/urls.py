from django.urls import path
from . import views

urlpatterns = [
    path("course", views.CreateCourseView.as_view()),
    path("list_course", views.RetrieveCourse.as_view()),
    path("delete_course/<int:pk>", views.DeleteCourseView.as_view()),
    path("student", views.CreateStudentView.as_view()),
    path("list_student", views.RetrieveStudentView.as_view()),
    path("delete_student/<int:pk>", views.DeleteStudentView.as_view()),
    path("session", views.CreateSessionView.as_view()),
    path("list_session", views.RetrieveSessionView.as_view()),
    path("update_session/<int:pk>", views.UpdateSessionView.as_view()),
    # path("student_session/", views.RetrieveStudentSessionView.as_view()),
    path("delete_session/<int:pk>", views.DeleteSessionView.as_view()),
    path("attendance", views.CreateAttendanceView.as_view()),
    path("list_attendance/<int:pk>", views.RetrieveAttendanceView.as_view()),
    path("delete_attendance/<int:pk>", views.DeleteAttendanceView.as_view()),
]
