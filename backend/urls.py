from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('profiles.urls')),
    path('api/', include('api.urls')),
    path('company/', include('companies.urls')),
    path('position/', include('position.urls')),
    path('salary/', include('salaries.urls'))
]
