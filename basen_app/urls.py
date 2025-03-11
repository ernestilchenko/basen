from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('basen/', views.basen, name='basen'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('gallery/', views.gallery, name='gallery'),
    path('types-of-pools/', views.typesOfPools, name='types-of-pools'),
    path('example/', views.example, name='example')
]
