from django.contrib import admin
from .models import Employees

# # Register your models here.
# admin.site.register(Employees)

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name', 'email','designation','gender','profile_image','documents')