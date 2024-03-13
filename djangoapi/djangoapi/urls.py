from django.contrib import admin
from django.urls import path,include
from  courses.views import display,table_view,income,expense,calc
from database.views import home,display

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('display/',display,name='display')
]
