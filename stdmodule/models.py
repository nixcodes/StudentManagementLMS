from django.db import models

# Create your models here.
class Register(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    mark = models.CharField(max_length=255,default='0')

class Feedback(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)

class fileupload(models.Model):
    file = models.FileField()