from django.db import models

class Courses(models.Model):
    name=models.CharField(max_length=200)
    language=models.CharField(max_length=100)
    price=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Company_income(models.Model):
    Date=models.DateField()
    Grocery=models.IntegerField()
    Bakery=models.IntegerField()
    Clothes=models.IntegerField()
    Electronics=models.IntegerField()

class Company_expense(models.Model):
    Date=models.DateField()
    Staff=models.IntegerField()
    Rent=models.IntegerField()
    Total=models.IntegerField()
    Otherexpense=models.IntegerField()

class Calculations(models.Model):
    Date=models.DateField()
    Total_income=models.IntegerField()
    Total_expense=models.IntegerField()
    ProfitorLoss=models.CharField(max_length=10)
    Profit=models.IntegerField()
    Loss=models.IntegerField()
