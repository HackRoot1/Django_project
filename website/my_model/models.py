from django.db import models

# Create your models here.
class MyModel(models.Model):
    classes = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    subjects = models.CharField(max_length=50)