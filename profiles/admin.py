from django.contrib import admin
from .models import Profile, EducationInstitute, EducationLevel

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
     def has_delete_permission(self, request, obj=None):
        return True
admin.site.register(Profile, ProfileAdmin)
admin.site.register(EducationInstitute)
admin.site.register(EducationLevel)


