from django.http import HttpResponse
from django.shortcuts import render
from ecomsite.models import Employee

def home(request):
    emp = Employee.objects.all()
    context = {
        'emp':emp,
    }
    return render ( request, 'home.html' ,context)