from django.db import models

class FormItems(models.Model):
    name     =   models.CharField(max_length=50)
    aadhaar  =   models.DecimalField(decimal_places=0,max_digits=12)
    username =   models.CharField(max_length=25, null=True)
class Test1(models.Model):
    Test    =   models.CharField(max_length=50)
class Test2(models.Model):
    Test    =   models.CharField(max_length=50)
# Create your models here.