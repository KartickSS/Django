from django.contrib import admin
from .models import Courses,Company_income,Company_expense,Calculations

admin.site.register(Courses)
admin.site.register(Company_income)
admin.site.register(Company_expense)
admin.site.register(Calculations)