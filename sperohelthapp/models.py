from django.db import models

# Create your models here.

class Task(models.Model):
    hhc_id=models.CharField(max_length=50)
    patients_name=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=14)
    email=models.EmailField(max_length=50)
    location=models.CharField(max_length=500)
    is_deleted=models.CharField(max_length=10)
    