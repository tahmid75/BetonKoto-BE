from dis import dis
from django.contrib import admin
from .models import Company, District

# Register your models here.
admin.site.register(Company)
admin.site.register(District)
