from operator import mod
from statistics import mode
from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=200)
    headquarter = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    website = models.CharField(max_length=50, null = True, default='', blank=True)
    description = models.CharField(max_length=1000, null=True, default='', blank=True )

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
