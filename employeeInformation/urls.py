from django.urls import path  
from .views import EmployeeRetrieve, employee_list
    
urlpatterns = [  
    path('retrieve/', EmployeeRetrieve.as_view(), name = 'EmployeeRetrieve'),
    path('emplist', employee_list, name='emplist')
]  