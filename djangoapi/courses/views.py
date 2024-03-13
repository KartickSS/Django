from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from . models import Courses,Company_income,Company_expense,Calculations
from . serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date,datetime
from datetime import timedelta
from . forms import Income_table



def display(request):
        return render(request,'index.html')

@api_view(['GET','POST'])
def course_list(request):
    if request.method == 'GET':
        course=Courses.objects.all()
        serializer=CourseSerializer(course,many=True)
        return JsonResponse({'course':serializer.data},safe=False)
    if request.method == 'POST':
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def details(request,id):

    course=Courses.objects.get(pk=id)

    if request.method=='GET':
        serializer=CourseSerializer(course)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

def table_view(request):
    start_date = date(2024, 2, 1)
    end_date=date(2024,2,4)
    while start_date <= end_date:
        income = Company_income.objects.filter(Date=start_date).first()
        total_income = income.Grocery + income.Bakery + income.Clothes + income.Electronics
        print(total_income)

        expense = Company_expense.objects.filter(Date=start_date).first()
        total_expense = expense.Staff + expense.Rent + expense.Otherexpense
        print(total_expense)
        
        if total_income > total_expense:
            profits=Calculations.objects.create(
                Date=start_date,
                Total_income=total_income,
                Total_expense=total_expense,
                ProfitorLoss='Profit',
                Profit=total_income-total_expense,
                Loss=0

            )
        elif total_income < total_expense:
            loss=Calculations.objects.create(
                Date=start_date,
                Total_income=total_income,
                Total_expense=total_expense,
                ProfitorLoss='Loss',
                Profit=0,
                Loss=total_expense-total_income    
            )
        
        start_date += timedelta(days=1)
    table1_records = Company_expense.objects.filter(Date=start_date)
    total=[record.Total for record in table1_records]
    return render(request,'tabelview.html',{'table':table1_records})

def income(request):
    if request.method=="POST":
        date=request.POST.get('date')
        grocery=request.POST.get('grocery')
        bakery=request.POST.get('bakery')
        clothes=request.POST.get('clothes')
        electronics=request.POST.get('electronics')
        Company_income.objects.create(Date=date,Grocery=grocery,Bakery=bakery,Clothes=clothes,Electronics=electronics)
        return render(request,'expense.html',{'date':date})
    return render(request,'income.html')

def expense(request):
    if request.method=="POST":
        date=request.POST.get('date')
        staff=request.POST.get('staff')
        rent=request.POST.get('rent')
        other=request.POST.get('other')
        total =float(staff)+float(rent)+float(other)
        Company_expense.objects.create(Date=date,Staff=staff,Rent=rent,Total=total,Otherexpense=other)
        return render(request,'expense.html',{'date':date})
    return render(request,'expense.html')

def calc(request):
    incomes = Company_income.objects.all()
    dates = {str(income.Date) for income in incomes}

    calval=Calculations.objects.all()
    calcdates={str(i.Date) for i in calval}
    print(calcdates)

    for_dates = dates - calcdates
    for date in for_dates:

        cal_expense = Company_expense.objects.get(Date=date)
        total_expense=cal_expense.Total
        cal_income=Company_income.objects.get(Date=date)
        total_income=cal_income.Grocery + cal_income.Bakery + cal_income.Clothes + cal_income.Electronics
            
        if total_income > total_expense:
            original_date = datetime.strptime(date, '%Y-%m-%d').date()
            Calculations.objects.create(
                Date=original_date,
                Total_income=total_income,
                Total_expense=total_expense,
                ProfitorLoss='Profit',
                Profit=total_income-total_expense,
                Loss=0
            )
        elif total_income < total_expense:
            original_date = datetime.strptime(date, '%Y-%m-%d').date()
            Calculations.objects.create(
                Date=original_date,
                Total_income=total_income,
                Total_expense=total_expense,
                ProfitorLoss='Loss',
                Profit=0,
                Loss=total_expense-total_income
            )
    calcs=Calculations.objects.all()
    return render(request,'calculation.html',{'calcs':calcs})




    
    

    """Calculations.objects.create(Date=date,Total_income=total_income,Total_expense=total_expense,ProfitorLoss=)"""



    """incomes = Company_income.objects.filter(Date=date)
        expenses = Company_expense.objects.filter(Date=date)

        total_income = sum([income.Grocery + income.Bakery + income.Clothes + income.Electronics for income in incomes])
        total_expense = sum([expense.Staff + expense.Rent + expense.Otherexpense for expense in expenses])

        if total_income > total_expense:
            Calculations.objects.create(
                Date=date,
                Total_income=total_income,
                Total_expense=total_expense,
                ProfitorLoss='Profit',
                Profit=total_income - total_expense,
                Loss=0 
            )
        elif total_expense > total_income:
            Calculations.objects.create(
                Date=date,
                Total_income=total_income,
                Total_expense=total_expense,
                ProfitorLoss='Loss',
                Profit=0,
                Loss=total_expense - total_income
            )
        return HttpResponse('success')

    return render(request, 'calculation.html')"""


    

    
    
    