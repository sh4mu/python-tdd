from django.urls import path
from employees import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
]