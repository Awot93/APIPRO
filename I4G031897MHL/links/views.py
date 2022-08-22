from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LinkSerializer
from .models import Link
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.

class PostListApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer