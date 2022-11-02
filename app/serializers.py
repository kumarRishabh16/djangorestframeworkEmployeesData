from rest_framework import serializers
from .models import *

class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
