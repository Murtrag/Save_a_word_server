from django.urls import path, include
from . import views
from api import urls

urlpatterns = [
    path('', views.hello_world)
]
