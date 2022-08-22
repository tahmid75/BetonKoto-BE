from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createProfile, name='createProfile'),
    path('view/', views.viewProfile, name='viewProfile'),
    path('update/', views.updateProfile, name='updateProfile'),
]
