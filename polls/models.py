from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    rollNo=models.BigIntegerField(primary_key=True)

class teacher(models.Model):
    name=models.CharField(max_length=30)
    id=models.IntegerField(primary_key=True)