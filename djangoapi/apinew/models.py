from django.db import models

class person(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField()
    Contact=models.BigIntegerField()
    Gender=models.CharField(max_length=10)