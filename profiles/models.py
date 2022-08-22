from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from companies.models import Company
from position.models import Position, Level

# Create your models here.

class EducationLevel(models.Model):
    level = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Education Level"

    def __str__(self):
           return  str(self.level)

class EducationInstitute(models.Model):
    name = models.CharField(max_length=100) 

    class Meta:
        verbose_name = "Educational Institute"

    def __str__(self):
           return  str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=16)
    gender = models.IntegerField(null=True,)
    educationLevel = models.ForeignKey(EducationLevel, null=True,  on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    salary = models.IntegerField(null=True,)
    educationInstitute = models.ForeignKey(EducationInstitute, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add = True, null=True )

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
           return  str(self.user)
    

