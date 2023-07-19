from django.shortcuts import render
from django.views.generic.list import ListView
from .models import EmployeeData
# Create your views here.

class EmployeeRetrieve(ListView):
    model = EmployeeData


def employee_list(request):
    emp_list = EmployeeData.objects.all()
    return render(request, 'employeelist.html', {'emp_list': emp_list})