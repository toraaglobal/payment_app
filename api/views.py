from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import UserSerializer
from userauths.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )