from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from base.serializers import (
    CourseSerializer,
    SessionSerializer,
    AttendanceSerializer,
)
from base.models import Course, Session, Attendance
from account.models import Account
from account.serializers import StudentAccountSerializer


# Create your views here.
class CreateCourseView(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class RetrieveCourse(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer

    def get_queryset(self):
        lecturer = self.request.user
        return Course.objects.filter(lecturer=lecturer)


class DeleteCourseView(generics.DestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CreateSessionView(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SessionSerializer
    queryset = Session.objects.all()


class RetrieveSessionView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SessionSerializer

    def get_queryset(self):
        lecturer = self.request.user
        return Session.objects.filter(lecturer=lecturer)


class RetrieveStudentSessionView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SessionSerializer

    def get_queryset(self):
        program = self.request.user.program
        return Session.objects.filter(program=program, status=True)


class UpdateSessionView(generics.UpdateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SessionSerializer
    queryset = Session.objects.all()


class DeleteSessionView(generics.DestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SessionSerializer
    queryset = Session.objects.all()


class CreateAttendanceView(generics.CreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()


class RetrieveAttendanceView(generics.ListAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        session = self.kwargs.get("pk")
        return Attendance.objects.filter(session=session)


class DeleteAttendanceView(generics.DestroyAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
