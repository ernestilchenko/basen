from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('basen/', views.basen, name='basen')
]
