from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from base.serializers import StudentSerializer, CourseSerializer
from base.models import Student, Course


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
