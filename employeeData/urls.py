from django.urls import path  
from .views import EmployeeCreate  
    
urlpatterns = [  
    path('create', EmployeeCreate.as_view(), name = 'EmployeeCreate')  
]  