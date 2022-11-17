from django.shortcuts import render
from .models import Post
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny] #FIXME 