from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewset) # posts가 기본 이름

urlpatterns=[
    path('api/', include(router.urls)),
]