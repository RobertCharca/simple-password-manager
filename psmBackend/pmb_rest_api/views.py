from django.shortcuts import render

#All about rest_framework
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response

# Create your views here.
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users_us.objects.all()
    permission_classes = [permissions.AllowAny]