from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    roll_no= models.PositiveIntegerField()
    strd  = models.CharField(   max_length=50)




