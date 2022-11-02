from django.shortcuts import render
from rest_framework.response import Response
from .models import Employees
from .serializers import EmployeesSerializers
from rest_framework import status
from rest_framework.views import APIView

class EmployeesList(APIView):
    def get(self, request, format=None):
        employees = Employees.objects.all()
        serializer = EmployeesSerializers(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeesSerializers(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'employees': serializer.data, 'status': status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


