from django.urls import path
from . import views

app_name = 'App_Post'

urlpatterns = [
    path('', views.home, name='home'),
]
