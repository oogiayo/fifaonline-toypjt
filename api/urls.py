from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('meta/<name>/', views.player, name='player'),
    path('user/<nickname>/', views.user, name='user'),
]
