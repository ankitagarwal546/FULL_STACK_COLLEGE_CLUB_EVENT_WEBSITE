from django.urls import path
from . import views

app_name = 'clubs'

urlpatterns = [
    path('', views.clubs_list, name='clubs_list'),
]
