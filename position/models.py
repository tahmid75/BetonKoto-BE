from django.db import models

# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=100)  
    def __str__(self):
           return  str(self.name)

class Level(models.Model):
    level = models.IntegerField()
    def __str__(self):
           return  str(self.level)