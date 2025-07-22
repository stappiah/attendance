# In your app's serializers.py
from rest_framework import serializers
from .models import Account
from rest_framework.authtoken.models import Token


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Account
        fields = (
            "email",
            "first_name",
            "last_name",
            # "user_type",
            # "program",
            # "index_number",
            "password",
            "password2",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.get("password")
        password2 = validated_data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match"})

        user = Account(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            # user_type=validated_data["user_type"],
            # program=validated_data["program"],
            # index_number=validated_data["index_number"],
        )

        user.set_password(password)
        user.save()

        Token.objects.create(user=user)
        return user

    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key


# class StudentAccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = (
#             "id",
#             "email",
#             "first_name",
#             "last_name",
#             # "user_type",
#             "program",
#             "index_number",
#         )
