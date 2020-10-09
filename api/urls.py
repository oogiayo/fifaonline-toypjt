from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('<int:player_id>/', views.player, name='player'),
]
