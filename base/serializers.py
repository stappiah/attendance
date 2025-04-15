from rest_framework import serializers
from base.models import Student, Course
from account.models import Account


class StudentSerializer(serializers.ModelSerializer):
    lecturer = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lecturer = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Course
        fields = "__all__"
