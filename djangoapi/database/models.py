from django.db import models

class Member(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    passwd=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.fname + ' ' + self.lname
    
    class Meta:
        indexes=[models.Index(fields=['fname','email'])]
