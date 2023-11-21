from django.shortcuts import render,get_object_or_404
from ecomsite.models import Employee
from django.http import Http404,HttpResponse


# Create your views here.
def employee_details(request,pk):
    Cand = get_object_or_404(Employee,pk=pk)
    context1 = {
        'employee':Cand,
    }
    return render(request,'employee_detail.html',context1)