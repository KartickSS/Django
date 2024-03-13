from django.shortcuts import render,redirect
from . models import Member
from . forms import Memberforms

def home(request):
    if request.method == "POST":
        form=Memberforms(request.POST or None)
        if form.is_valid():
            form.save()
            print('success')
        return redirect(display)
    return render(request,'dbhome.html',{})

def display(request):
    objs=Member.objects.all()
    return render(request,'dbdisplay.html',{'objs':objs})


def new(request):
    pass
