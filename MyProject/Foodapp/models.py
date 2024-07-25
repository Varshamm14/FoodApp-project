from django.db import models
from django.db import connection

# Create your models here.
class Details(models.Model):
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)