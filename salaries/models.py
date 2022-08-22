from operator import mod
from tabnanny import verbose
from django.db import models
from companies.models import Company, District
from position.models import Position, Level
from django.contrib.auth.models import User

# Create your models here.
class Salary(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL,null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL,null=True)
    location = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    salary = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"

    def __str__(self):
           return  str( self.user)