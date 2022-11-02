from django.urls import path
from .views import EmployeesList
from . import views

urlpatterns = [
    path('employees/', views.EmployeesList.as_view()),

]

