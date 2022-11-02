from django.db import models

Designation= (
    (
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('Designer', 'Designer'),
        ('Architect', 'Architect'),
        ('Team Lead', 'Team Lead'),
        ('Project Manager', 'Project Manager'),
        ('Business Analyst', 'Business Analyst'),
        ('HR', 'HR'),
        ('Admin', 'Admin'),
        ('Other', 'Other'),
    )
)

class Employees(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    first_name= models.CharField(max_length=14)
    last_name = models.CharField(max_length=14)
    email = models.EmailField()
    designation = models.CharField(choices=Designation, max_length=100)
    gender= models.CharField(max_length=1)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    documents = models.FileField(upload_to='documents', blank=True)
