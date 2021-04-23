from django.urls import path, include
from . import views
from api import urls


from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'words', views.WordViewSet, basename="words")
router.register(r'language', views.LanguageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
