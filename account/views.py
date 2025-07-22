from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, authentication, status
from .serializers import (
    AccountSerializer,
)
from .models import Account
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import check_password


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Manually create a token for the user
        token, created = Token.objects.get_or_create(user=user)

        # Customize the response to include the user details and token
        return Response(
            {
                "user": {
                    "user_id": user.pk,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    # "user_type": user.user_type,
                    # "program": user.program,
                    # "index_number": user.index_number,
                },
                "token": token.key,
            }
        )


class CustomAuthModel(ObtainAuthToken):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                # "user_type": user.user_type,
                # "index_number": user.index_number,
                # "program": user.program,
                "token": token.key,
                "user_id": user.pk,
            }
        )
