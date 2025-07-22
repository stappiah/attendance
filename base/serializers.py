from rest_framework import serializers
from base.models import Course, Session, Attendance, Student
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


class SessionSerializer(serializers.ModelSerializer):
    lecturer = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all(), default=serializers.CurrentUserDefault()
    )
    session_course = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    get_program = serializers.ReadOnlyField()
    get_student = serializers.ReadOnlyField()
    get_index_number = serializers.ReadOnlyField()

    class Meta:
        model = Attendance
        fields = "__all__"
