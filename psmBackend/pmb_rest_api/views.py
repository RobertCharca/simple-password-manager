from django.shortcuts import render

#All about rest_framework
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response

# Create your views here.
#All about users
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users_us.objects.all()
    permission_classes = [permissions.AllowAny]

#All about categories
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category_cat.objects.all()
    permission_classes = [permissions.AllowAny]

#All about items
#Webpages
class ItemWebPageViewSet(viewsets.ModelViewSet):
    serializer_class = ItemWebPageSerializer
    queryset = ItemWebPage_iwp.objects.all()
    permission_classes = [permissions.AllowAny]

#Payment cards
class ItemPaymentCardViewSet(viewsets.ModelViewSet):
    serializer_class = ItemPaymentCardSerializer
    queryset = ItemPaymentCard_ipc.objects.all()
    permission_classes = [permissions.AllowAny]