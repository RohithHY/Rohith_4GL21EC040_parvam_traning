from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    teaher_id = models.IntegerField(max_length=20, unique=True)
    qualification = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name