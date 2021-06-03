
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ping', views.ping, name='ping'),
    path('getusers', views.getusers, name='getusers'),
    path('getusersj', views.getusersj, name='getusersj'),
]
