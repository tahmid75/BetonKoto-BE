from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('all/', views.allCompanies, name='allCompanies'),
    path('allTrimmed/', views.allCompaniesTrimmed, name='allCompaniesTrimmed'),
    path('<int:id>', views.companyDetails, name='companyDetails'),

    path('locations/', views.allLocations, name='allLocations')
]