from django.db import models

# Create your models here.
class MyModel(models.Model):
    classes = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    semester = models.CharField(max_length=50, null = True)
    subjects = models.CharField(max_length=50)
    subject_link = models.CharField(max_length=100, null=True)